from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QGraphicsItem
from PySide2.QtGui import QImage, QPixmap
import cv2
from ui.mainwindow import Ui_cvPlot

class picturezoom(QMainWindow, Ui_cvPlot, QGraphicsView):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(picturezoom, self).__init__(parent)

        self.setupUi(self)
        self.graphicsView.setDragMode(QGraphicsView.RubberBandDrag)  # 设置图元的拖动属性
        self.graphicsView.setAcceptDrops(True)  # 此窗口小部件启用了放置事件
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.picshow.setDragEnable
        # self.setDragEnabled(True)
        # picture_work_dir = 'Manual_mode_bmp'
        img = cv2.imread("imgs/img.png")  # 读取图像，Manual_mode_bmp为文件夹
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道

        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]

        self.zoomscale = 1  # 图片放缩尺度
        print(type(img))
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setFlag(QGraphicsItem.ItemIsMovable)  # 使图元可以拖动，非常关键！！！！！
        self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)  # 将图元添加到场景中
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图  picshow为graphicsView视图

    @Slot()
    def on_zoomin_clicked(self):
        """
        点击缩小图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale - 0.05
        if self.zoomscale <= 0:
            self.zoomscale = 0.2
        self.item.setScale(self.zoomscale)  # 缩小图像

    @Slot()
    def on_zoomout_clicked(self):
        """
        点击方法图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale + 0.05
        if self.zoomscale >= 1.2:
            self.zoomscale = 1.2
        self.item.setScale(self.zoomscale)  # 放大图像

        def dragLeaveEvent(self, event):
            self.dragOver = False
            self.update()

        def dropEvent(self, event):
            self.dragOver = False
            self.update()


def main():
    import sys
    app = QApplication(sys.argv)
    piczoom = picturezoom()
    piczoom.show()
    app.exec_()


if __name__ == '__main__':
    main()