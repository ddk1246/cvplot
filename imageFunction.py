import cv2
import numpy as np

class imageHandle(object):
    def __init__(self,model,*args):
        self.net = cv2.dnn.readNetFromTensorflow(model)

    def rotate_bound(self,image, angle):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        # grab the rotation matrix (applying the negative of the
        # angle to rotate clockwise), then grab the sine and cosine
        # (i.e., the rotation components of the matrix)
        M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)

        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY

        # perform the actual rotation and return the image
        return cv2.warpAffine(image, M, (nW, nH))

    def findSubImg(self,image, maskSize, threshold):
        image = cv2.GaussianBlur(image, (3, 3), 1)
        gray = image
        if len(image.shape) != 2:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imgH, imgW = gray.shape[:2]
        ret, binary1 = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        ret, binary2 = cv2.threshold(gray, threshold, 255, cv2.THRESH_TRUNC)
        binary = cv2.bitwise_or(binary1, binary2)

        m = np.ones_like(binary)
        m[:, :] = 255

        m[maskSize:imgH - maskSize, maskSize:imgW - maskSize] = 0
        dst = cv2.bitwise_or(binary, m)

        dstNot = cv2.bitwise_not(binary1)
        contours, hierarchy = cv2.findContours(dstNot, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        subImgLocation = []
        for i, cnt in enumerate(contours):
            if cv2.contourArea(cnt) < 50:
                continue
            cv2.drawContours(image, contours, i, (255, 0, 0), 1)
            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            (x, y, w, h) = cv2.boundingRect(cnt)
            subImgLocation.append((x, y, w, h))
            cv2.rectangle(image, (x, y), (x + w, y + h), (100, 255, 30), 2)

            mm = cv2.moments(cnt)

            cx = int(mm['m10'] / mm['m00'])
            cy = int(mm['m01'] / mm['m00'])
            cv2.circle(image, (cx, cy), 3, (0, 100, 255), -1)

        subImgLocation.sort(key=lambda x: x[0] / imgW * 8 + x[1] / imgH)
        print("Number of Contours is", len(subImgLocation))
        return subImgLocation, image, dst

    def subImgAffine(self,img,**shape):
        subImgLocation, outImage, dst = self.findSubImg(img, 20, 150)
        subImgList = []
        imgInputSize = (28, 28)
        r = 0.9
        for k, v in enumerate(subImgLocation):
            '''
                仿射变换法:完全提出框选数字
            '''
            (x, y, w, h) = v
            preImg = dst[y:y + h, x:x + w]
            preImg = cv2.bitwise_not(preImg)

            matSrc = np.float32([[0, 0], [w, 0], [w, h]])  # 需要注意的是 行列 和 坐标 是不一致的
            matDst = np.float32([[imgInputSize[1]/2*(1 - w / np.linalg.norm((w, h))  * r), imgInputSize[0]/2*(1 - h / np.linalg.norm((w, h))  * r)],
                                 [imgInputSize[1]/2*(1 + w / np.linalg.norm((w, h))  * r), imgInputSize[0]/2*(1 - h / np.linalg.norm((w, h))  * r)],
                                 [imgInputSize[1]/2*(1 + w / np.linalg.norm((w, h))  * r), imgInputSize[0]/2*(1 + h / np.linalg.norm((w, h))  * r)],
                                 ])
            matAffine = cv2.getAffineTransform(matSrc, matDst)  # mat 1 src 2 dst 形成组合矩阵
            preImg = cv2.warpAffine(preImg, matAffine, imgInputSize)
            subImgList.append(preImg)
        subImgList = np.array(subImgList).reshape(-1, 28, 28, 1)
        return subImgList

    def singleImg2num(self,img):
        self.net.setInput(cv2.dnn.blobFromImage(img, 1.0 /255.0, (28, 28), (0, 0, 0), swapRB=True, crop=False))
        cvOut = self.net.forward()
        return cvOut