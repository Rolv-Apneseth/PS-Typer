# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultWindow(object):
    def setupUi(self, resultWindow):
        resultWindow.setObjectName("resultWindow")
        resultWindow.resize(803, 322)
        resultWindow.setAcceptDrops(True)
        resultWindow.setStyleSheet("QWidget {\n"
"    background: rgb(50, 50, 50);\n"
"    color: rgb(235, 235, 235);\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QFrame {    \n"
"    border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton, QComboBox {    \n"
"    background: rgb(70, 70, 70);\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton::hover, QComboBox::hover {\n"
"    background: rgb(90, 90, 90)\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(resultWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(resultWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelAccuracy = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAccuracy.sizePolicy().hasHeightForWidth())
        self.labelAccuracy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelAccuracy.setFont(font)
        self.labelAccuracy.setStyleSheet("font-size: 24pt;")
        self.labelAccuracy.setWordWrap(True)
        self.labelAccuracy.setObjectName("labelAccuracy")
        self.verticalLayout_3.addWidget(self.labelAccuracy)
        self.labelSpeed = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSpeed.sizePolicy().hasHeightForWidth())
        self.labelSpeed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelSpeed.setFont(font)
        self.labelSpeed.setStyleSheet("font-size: 24pt;")
        self.labelSpeed.setWordWrap(True)
        self.labelSpeed.setObjectName("labelSpeed")
        self.verticalLayout_3.addWidget(self.labelSpeed)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.labelHighscoreSet = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighscoreSet.sizePolicy().hasHeightForWidth())
        self.labelHighscoreSet.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelHighscoreSet.setFont(font)
        self.labelHighscoreSet.setStyleSheet("font-weight: bold; font-size: 24pt;")
        self.labelHighscoreSet.setWordWrap(True)
        self.labelHighscoreSet.setObjectName("labelHighscoreSet")
        self.verticalLayout.addWidget(self.labelHighscoreSet)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonMainMenu = QtWidgets.QPushButton(resultWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonMainMenu.setFont(font)
        self.buttonMainMenu.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayout.addWidget(self.buttonMainMenu)
        self.buttonNext = QtWidgets.QPushButton(resultWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNext.sizePolicy().hasHeightForWidth())
        self.buttonNext.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonNext.setFont(font)
        self.buttonNext.setObjectName("buttonNext")
        self.horizontalLayout.addWidget(self.buttonNext)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.retranslateUi(resultWindow)
        QtCore.QMetaObject.connectSlotsByName(resultWindow)

    def retranslateUi(self, resultWindow):
        _translate = QtCore.QCoreApplication.translate
        resultWindow.setWindowTitle(_translate("resultWindow", "Result"))
        self.labelAccuracy.setText(_translate("resultWindow", "Your accuracy: 100%"))
        self.labelSpeed.setText(_translate("resultWindow", "Your speed:      50wpm"))
        self.labelHighscoreSet.setText(_translate("resultWindow", "You set an all time highscore!"))
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
