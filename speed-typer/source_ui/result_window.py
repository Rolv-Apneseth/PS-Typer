# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultWindow(object):
    def setupUi(self, resultWindow):
        resultWindow.setObjectName("resultWindow")
        resultWindow.resize(625, 478)
        resultWindow.setAcceptDrops(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(resultWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(resultWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 603, 456))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(600, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.labelHighscoreSet = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighscoreSet.sizePolicy().hasHeightForWidth())
        self.labelHighscoreSet.setSizePolicy(sizePolicy)
        self.labelHighscoreSet.setMinimumSize(QtCore.QSize(470, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelHighscoreSet.setFont(font)
        self.labelHighscoreSet.setStyleSheet("")
        self.labelHighscoreSet.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHighscoreSet.setWordWrap(True)
        self.labelHighscoreSet.setObjectName("labelHighscoreSet")
        self.verticalLayout_2.addWidget(self.labelHighscoreSet)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.labelSpeed = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSpeed.sizePolicy().hasHeightForWidth())
        self.labelSpeed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelSpeed.setFont(font)
        self.labelSpeed.setStyleSheet("")
        self.labelSpeed.setWordWrap(True)
        self.labelSpeed.setObjectName("labelSpeed")
        self.horizontalLayout_3.addWidget(self.labelSpeed)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.labelAccuracy = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAccuracy.sizePolicy().hasHeightForWidth())
        self.labelAccuracy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelAccuracy.setFont(font)
        self.labelAccuracy.setStyleSheet("")
        self.labelAccuracy.setWordWrap(True)
        self.labelAccuracy.setObjectName("labelAccuracy")
        self.horizontalLayout_3.addWidget(self.labelAccuracy)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.buttonMainMenu = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMainMenu.sizePolicy().hasHeightForWidth())
        self.buttonMainMenu.setSizePolicy(sizePolicy)
        self.buttonMainMenu.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonMainMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonMainMenu.setAutoDefault(True)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayout_2.addWidget(self.buttonMainMenu)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.buttonNext = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNext.sizePolicy().hasHeightForWidth())
        self.buttonNext.setSizePolicy(sizePolicy)
        self.buttonNext.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonNext.setFont(font)
        self.buttonNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonNext.setAutoDefault(False)
        self.buttonNext.setDefault(True)
        self.buttonNext.setObjectName("buttonNext")
        self.horizontalLayout_2.addWidget(self.buttonNext)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(resultWindow)
        QtCore.QMetaObject.connectSlotsByName(resultWindow)

    def retranslateUi(self, resultWindow):
        _translate = QtCore.QCoreApplication.translate
        resultWindow.setWindowTitle(_translate("resultWindow", "Result"))
        self.labelHighscoreSet.setText(_translate("resultWindow", "You set an all time highscore!"))
        self.labelSpeed.setText(_translate("resultWindow", "50 WPM"))
        self.labelAccuracy.setText(_translate("resultWindow", "100%"))
        self.buttonMainMenu.setText(_translate("resultWindow", "Main Menu"))
        self.buttonNext.setText(_translate("resultWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultWindow = QtWidgets.QWidget()
    ui = Ui_resultWindow()
    ui.setupUi(resultWindow)
    resultWindow.show()
    sys.exit(app.exec_())
