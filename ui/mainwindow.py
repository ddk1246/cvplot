# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun Jul  4 22:43:59 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_cvPlot(object):
    def setupUi(self, cvPlot):
        cvPlot.setObjectName("cvPlot")
        cvPlot.resize(965, 739)
        self.centralwidget = QtWidgets.QWidget(cvPlot)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.caplabel = QtWidgets.QLabel(self.groupBox)
        self.caplabel.setObjectName("caplabel")
        self.horizontalLayout_7.addWidget(self.caplabel)
        self.caplist = QtWidgets.QComboBox(self.groupBox)
        self.caplist.setObjectName("caplist")
        self.horizontalLayout_7.addWidget(self.caplist)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(112, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.opencap = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opencap.sizePolicy().hasHeightForWidth())
        self.opencap.setSizePolicy(sizePolicy)
        self.opencap.setObjectName("opencap")
        self.horizontalLayout.addWidget(self.opencap)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(2, 7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_6.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setContentsMargins(-1, 12, -1, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.grab = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grab.sizePolicy().hasHeightForWidth())
        self.grab.setSizePolicy(sizePolicy)
        self.grab.setObjectName("grab")
        self.horizontalLayout_3.addWidget(self.grab)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 7)
        cvPlot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cvPlot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        cvPlot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cvPlot)
        self.statusbar.setObjectName("statusbar")
        cvPlot.setStatusBar(self.statusbar)
        self.actionfromfile = QtWidgets.QAction(cvPlot)
        self.actionfromfile.setObjectName("actionfromfile")
        self.actionexit = QtWidgets.QAction(cvPlot)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionfromfile)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(cvPlot)
        QtCore.QMetaObject.connectSlotsByName(cvPlot)

    def retranslateUi(self, cvPlot):
        cvPlot.setWindowTitle(QtWidgets.QApplication.translate("cvPlot", "cvplot", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("cvPlot", "视频流", None, -1))
        self.caplabel.setText(QtWidgets.QApplication.translate("cvPlot", "摄像头:", None, -1))
        self.opencap.setText(QtWidgets.QApplication.translate("cvPlot", "开启", None, -1))
        self.grab.setText(QtWidgets.QApplication.translate("cvPlot", "抓取", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("cvPlot", "识别", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("cvPlot", "首选项", None, -1))
        self.actionfromfile.setText(QtWidgets.QApplication.translate("cvPlot", "从文件", None, -1))
        self.actionexit.setText(QtWidgets.QApplication.translate("cvPlot", "exit", None, -1))

