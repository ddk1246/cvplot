# #--------------------------------------------------
# import ctypes
#
# lib = ctypes.cdll.LoadLibrary("lib/caplist.dll")
# result = ctypes.create_string_buffer(512, "\0")
# lib.listDevices.argtypes = [ctypes.c_char_p,ctypes.c_int32]
# lib.listDevices(result,512)
#
# print(result.value.decode("utf8"))
#
# a=[]
# # print(lib.SUM(1,2))
# #--------------------------------------------------

# #--------------------------------------------------
# import cv2
# import matplotlib.pyplot as plt
#
# img2 = cv2.imread(r"C:\Users\10055\Desktop\k.jpg")
# h,w,d = img2.shape
# img2 = cv2.resize(img2,(w//5,h//5))
# cv2.imshow("aaa",img2)
# cv2.waitKey(0)
# cv2.imwrite("kk.jpg",img2)
# print(img2.shape)
# #--------------------------------------------------

# #--------------------------------------------------
# class Person(object):
#     def __init__(self, name, age, **kw):  # **kw代表不确定参数
#         self.name = name
#         self.age = age
#         for k, v in kw.items():  # 遍历赋值 **kw相当于dict，遍历取key，value
#             setattr(self, k, v)
#             print(k, v)
#
#
# p = Person("Lisa", 18, address='china', gender='female')
# print(p.address)
# print(p.gender)
# #--------------------------------------------------

# #--------------------------------------------------
# import cv2
# img = cv2.imread("img.png",0)
# net = cv2.dnn.readNet("./model/model.pb",'')
#
# rows = img.shape[0]
# cols = img.shape[1]
# net.setInput(cv2.dnn.blobFromImage(img, 1.0/127.5, (28, 28), (127.5, 127.5, 127.5), swapRB=True, crop=False))
# cvOut = net.forward()
# print(cvOut.shape)
# for detection in cvOut[0,:]:
#     score = float(detection)
#     print(score)
#     if score > 0.3:
#         left = detection[3] * cols
#         top = detection[4] * rows
#         right = detection[5] * cols
#         bottom = detection[6] * rows
#         cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
# cv2.imshow('img', img)
# #--------------------------------------------------

# #--------------------------------------------------
# import cv2
# import numpy as np
#
# src = cv2.imread("imgs/xx.bmp")
# h, w = src.shape[:2]
# src = cv2.resize(src,(w//2,h//2))
# A = cv2.getPerspectiveTransform(
#     np.array([[0, 0], [w, 0], [0, h], [w, h]], np.float32),
#     np.array([[w / 2, 0], [w, 0], [0, h], [w, h / 2.0]], np.float32))
# print(A)
# B = np.array([[1,0.1,0],
#               [0.1,1,0],
#               [0,0,1]])
# image = cv2.warpPerspective(src, B, (w, h))
# cv2.imshow("image",image)
# cv2.waitKey(0)
# # cv2.findHomography()

# #--------------------------------------------------

# #--------------------------------------------------
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

file = r'C:\Users\10055\Desktop\kk.jpg'
holistic = mp_holistic.Holistic(static_image_mode=True)

image = cv2.imread(file)
image_hight, image_width, _ = image.shape
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = holistic.process(image)
# #--------------------------------------------------

# #--------------------------------------------------
class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.actionfileopen.triggered.connect(self.open_file)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        print(fileName)
        print(fileType)




