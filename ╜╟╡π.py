import cv2
import numpy as np
import matplotlib.pyplot as plt

MIN_MATCH_COUNT = 12

img1 = cv2.imread('imgs/yida.png',0)
img2 = cv2.imread('imgs/yida_in_dsk.jpg',0)
h,w =img2.shape
img2 = cv2.resize(img2,(w//5,h//5))
sift = cv2.SIFT_create()
# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# kp = sift.detect(gray, None)  # 找到关键点

# cv2.drawKeypoints(gray, kp, img1)  # 绘制关键点

# cv2.imshow('sp', img1)
# cv2.waitKey(0)

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)


# store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)
print(good)

if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h, w = img1.shape
    pts = np.float32([[0, 0], [0, h ], [w , h ], [w , 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)

    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

else:
    print(
        "Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
    matchesMask = None

draw_params = dict(#matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   matchesMask=matchesMask,  # draw only inliers
                   flags=2)

bf = cv2.BFMatcher()
# 获得匹配的结果
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)
for dst in good:
    print(dst.distance)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:8], None, flags=2)
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,matchesMask = matchesMask,flags=2)
# img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

plt.imshow(img3, 'gray'), plt.show()
