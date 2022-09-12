from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QShortcut, \
    QTextBrowser, QPushButton, QWidget, QMenu, QGraphicsPixmapItem, QMessageBox, QGraphicsItem
from PySide2.QtGui import QColor, QKeySequence, QCursor, QIcon, QImage, QPixmap
from PySide2 import QtCore
from PySide2.QtCore import Signal, QObject, QStringListModel, QPoint, QThread
from ui.mainwindow import Ui_cvPlot
from imageFunction import imageHandle
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg

import matplotlib.pyplot as plt
import cv2
import sys
import ctypes
import threading
import time



class MyFigure(FigureCanvas):
    def __init__(self, width, height, dpi=100):
        # 创建一个Figure,该Figure为matplotlib下的Figure，不是matplotlib.pyplot下面的Figure
        self.fig = plt.figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        # 在父类中激活Figure窗口，此句必不可少，否则不能显示图形
        super(MyFigure, self).__init__(self.fig)


class WorkThread(QThread):  # 多线程核心，非常重要
    # 定义一个信号
    trigger = Signal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        self.trigger.emit('')  # 不知道为什么这样写，照葫芦画瓢


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()  # 调用父类初始化函数
        self.ui = Ui_cvPlot()  # 继承UI界面
        self.ui.setupUi(self)  # ui界面初始化
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.signalAndSlotInit()
        self.ui.graphicsView.setDragMode(QGraphicsView.RubberBandDrag)  # 设置图元的拖动属性
        self.ui.graphicsView.setAcceptDrops(True)  # 此窗口小部件启用了放置事件
        self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)

        self.cap = cv2.VideoCapture()

        lib = ctypes.cdll.LoadLibrary("lib/caplist.dll")
        result = ctypes.create_string_buffer(512, "\0")
        lib.listDevices.argtypes = [ctypes.c_char_p, ctypes.c_int32]
        lib.listDevices(result, 512)
        self.ui.caplist.addItem(result.value.decode("utf8"))

        self.testAPP()
        # self.ui.grab.setEnabled(False)
        # self.ui.pushButton.setEnabled(False)

    def testAPP(self):
        src = cv2.imread("imgs/img_2.png")
        self.plotQImage([src])
        # imghd =  imageHandle("./model/model.pb")
        # src = imghd.rotate_bound(src,0)
        # imglist = imghd.subImgAffine(src)
        # self.plotImage(imglist)
        # tel = ""
        # for i in imglist:
        #     out = imghd.singleImg2num(i)
        #     out = np.argmax(out[0,:])
        #     tel += str(out)
        # self.ui.textBrowser.setText(str(tel))

    def RGBImgShow(self):
        src = cv2.imread("imgs/img.png")
        self.plotImage(src)
        print(f"[INFO] {sys._getframe().f_code.co_name} callBack")

    def plotImage(self, imgList, swapRB=True, isVideo=False):
        if not len(imgList):
            self.plotClear()
            return
        F = MyFigure(width=5, height=5)
        if not hasattr(imgList, "shape") or len(imgList.shape) >= 4:
            w = int(np.ceil(np.sqrt(len(imgList))))
            h = int(np.ceil(len(imgList) / w))
            for k, img in enumerate(imgList):
                F.fig.add_subplot(h, w, (k + 1))
                plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.1, wspace=0.1, hspace=0.1)
                plt.xticks([])
                plt.yticks([])
                plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
        else:
            if swapRB == True:
                img = cv2.cvtColor(imgList, cv2.COLOR_RGB2BGR)
            else:
                img = imgList
            F.fig.add_subplot(111)
            plt.axis('off')
            plt.imshow(img)
            # plt.close()

        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addWidget(F)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()

    def plotQImage(self, imgList, swapRB=True):
        if not len(imgList):
            self.plotClear()
            return
        F = MyFigure(width=5, height=5)
        if not hasattr(imgList, "shape") or len(imgList.shape) >= 4:
            w = int(np.ceil(np.sqrt(len(imgList))))
            h = int(np.ceil(len(imgList) / w))
            for k, img in enumerate(imgList):
                F.fig.add_subplot(h, w, (k + 1))
                plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.1, hspace=0.1)
                plt.xticks([])
                plt.yticks([])
                plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
        else:
            img = imgList
            F.fig.add_subplot(111)
            plt.axis('off')
            plt.imshow(img)
        plt.close()

        F.draw()
        img = np.array(F.renderer.buffer_rgba())
        if swapRB == True:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)
        h, w, _ = img.shape
        frame = QImage(img,w,h,QImage.Format_RGBA8888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setFlag(QGraphicsItem.ItemIsMovable)  # 使图元可以拖动，非常关键！！！！！
        self.item.setFlag(QGraphicsItem.ItemIsFocusable)  # 选择时出现虚线框
        self.item.setFlag(QGraphicsItem.ItemIsSelectable)  # 可选择
        self.item.setScale(1)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)  # 将图元添加到场景中
        self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图  picshow为graphicsView视图

    def plotClear(self):
        self.scene = QGraphicsScene()  # 创建场景
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()

    def openCapFunc(self):
        ret, frame = self.cap.read()
        self.plotImage(frame)

    def capCallbackFun(self):

        if self.timer_camera.isActive() == False:
            fl = self.cap.open(self.ui.caplist.currentIndex(), cv2.CAP_DSHOW)
            if fl:
                self.ui.opencap.setText("关闭")
                self.timer_camera.start(50)
                print(f"[INFO] {sys._getframe().f_code.co_name} callBack: CAPOPEN")
            else:
                msg = QMessageBox.warning(self, "warning", "请检查相机于电脑是否连接正确",
                                          buttons=QMessageBox.Ok)
        else:
            self.ui.opencap.setText("开启")
            self.timer_camera.stop()
            self.cap.release()  # 摄像头释放
            self.plotClear()
            print(f"[INFO] {sys._getframe().f_code.co_name} callBack: CAPCLOSE")

    def signalAndSlotInit(self):
        self.ui.grab.clicked.connect(self.RGBImgShow)
        self.ui.opencap.clicked.connect(self.capCallbackFun)
        self.timer_camera.timeout.connect(self.openCapFunc)

    def statusbarShow(self, string):
        self.ui.statusbar.showMessage(str(string), 0)


def main():
    app = QApplication([])

    mainw = MainWindow()
    mainw.show()

    app.exec_()


if __name__ == '__main__':
    main()
