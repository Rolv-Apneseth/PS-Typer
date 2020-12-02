# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(706, 214)
        mainWindow.setStyleSheet("QWidget {\n"
"    \n"
"    background: rgb(50, 50, 50);\n"
"    color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QFrame {    \n"
"    \n"
"    \n"
"    border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton, QComboBox {\n"
"    \n"
"    background: rgb(70, 70, 70)\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frameMainMenu = QtWidgets.QFrame(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMainMenu.sizePolicy().hasHeightForWidth())
        self.frameMainMenu.setSizePolicy(sizePolicy)
        self.frameMainMenu.setStyleSheet("")
        self.frameMainMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMainMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMainMenu.setObjectName("frameMainMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameMainMenu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelMainMenu = QtWidgets.QLabel(self.frameMainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMainMenu.sizePolicy().hasHeightForWidth())
        self.labelMainMenu.setSizePolicy(sizePolicy)
        self.labelMainMenu.setMinimumSize(QtCore.QSize(0, 40))
        self.labelMainMenu.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelMainMenu.setFont(font)
        self.labelMainMenu.setStyleSheet("font-weight: bold;")
        self.labelMainMenu.setObjectName("labelMainMenu")
        self.verticalLayout_2.addWidget(self.labelMainMenu)
        self.lineMainMenu = QtWidgets.QFrame(self.frameMainMenu)
        self.lineMainMenu.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineMainMenu.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineMainMenu.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineMainMenu.setObjectName("lineMainMenu")
        self.verticalLayout_2.addWidget(self.lineMainMenu)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelSelectMode = QtWidgets.QLabel(self.frameMainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSelectMode.sizePolicy().hasHeightForWidth())
        self.labelSelectMode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(False)
        self.labelSelectMode.setFont(font)
        self.labelSelectMode.setObjectName("labelSelectMode")
        self.horizontalLayout_6.addWidget(self.labelSelectMode)
        self.comboBoxSelectMode = QtWidgets.QComboBox(self.frameMainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelectMode.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectMode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxSelectMode.setFont(font)
        self.comboBoxSelectMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxSelectMode.setObjectName("comboBoxSelectMode")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.comboBoxSelectMode.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBoxSelectMode)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonStart = QtWidgets.QPushButton(self.frameMainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonStart.setFont(font)
        self.buttonStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonStart.setObjectName("buttonStart")
        self.horizontalLayout_5.addWidget(self.buttonStart)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.buttonSettings = QtWidgets.QPushButton(self.frameMainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)
        self.buttonSettings.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonSettings.setFont(font)
        self.buttonSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSettings.setObjectName("buttonSettings")
        self.horizontalLayout_5.addWidget(self.buttonSettings)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addWidget(self.frameMainMenu)
        self.frameHighscore = QtWidgets.QFrame(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHighscore.sizePolicy().hasHeightForWidth())
        self.frameHighscore.setSizePolicy(sizePolicy)
        self.frameHighscore.setAutoFillBackground(False)
        self.frameHighscore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHighscore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHighscore.setObjectName("frameHighscore")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameHighscore)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelHighscore = QtWidgets.QLabel(self.frameHighscore)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighscore.sizePolicy().hasHeightForWidth())
        self.labelHighscore.setSizePolicy(sizePolicy)
        self.labelHighscore.setMinimumSize(QtCore.QSize(0, 40))
        self.labelHighscore.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelHighscore.setFont(font)
        self.labelHighscore.setStyleSheet("font-weight: bold;")
        self.labelHighscore.setObjectName("labelHighscore")
        self.verticalLayout.addWidget(self.labelHighscore)
        self.lineHighscore = QtWidgets.QFrame(self.frameHighscore)
        self.lineHighscore.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineHighscore.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineHighscore.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineHighscore.setObjectName("lineHighscore")
        self.verticalLayout.addWidget(self.lineHighscore)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTodayTitle = QtWidgets.QLabel(self.frameHighscore)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTodayTitle.setFont(font)
        self.labelTodayTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTodayTitle.setObjectName("labelTodayTitle")
        self.horizontalLayout_2.addWidget(self.labelTodayTitle)
        self.labelTodayScore = QtWidgets.QLabel(self.frameHighscore)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.labelTodayScore.setFont(font)
        self.labelTodayScore.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTodayScore.setObjectName("labelTodayScore")
        self.horizontalLayout_2.addWidget(self.labelTodayScore)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelAlltimeTitle = QtWidgets.QLabel(self.frameHighscore)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelAlltimeTitle.setFont(font)
        self.labelAlltimeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlltimeTitle.setObjectName("labelAlltimeTitle")
        self.horizontalLayout_3.addWidget(self.labelAlltimeTitle)
        self.labelAlltimeScore = QtWidgets.QLabel(self.frameHighscore)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.labelAlltimeScore.setFont(font)
        self.labelAlltimeScore.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlltimeScore.setObjectName("labelAlltimeScore")
        self.horizontalLayout_3.addWidget(self.labelAlltimeScore)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addWidget(self.frameHighscore)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Speed Type Test"))
        self.labelMainMenu.setText(_translate("mainWindow", "Main Menu"))
        self.labelSelectMode.setText(_translate("mainWindow", "Mode:"))
        self.comboBoxSelectMode.setItemText(0, _translate("mainWindow", "Common Phrases"))
        self.comboBoxSelectMode.setItemText(1, _translate("mainWindow", "Famous Novel Excerpts"))
        self.comboBoxSelectMode.setItemText(2, _translate("mainWindow", "Famous Quotes/Speeches"))
        self.comboBoxSelectMode.setItemText(3, _translate("mainWindow", "Facts/Educational"))
        self.comboBoxSelectMode.setItemText(4, _translate("mainWindow", "Randomly Generated Text"))
        self.buttonStart.setText(_translate("mainWindow", "Begin"))
        self.buttonSettings.setText(_translate("mainWindow", "Settings"))
        self.labelHighscore.setText(_translate("mainWindow", "Highscores"))
        self.labelTodayTitle.setText(_translate("mainWindow", " Today: "))
        self.labelTodayScore.setText(_translate("mainWindow", "0 WPM"))
        self.labelAlltimeTitle.setText(_translate("mainWindow", " All-time: "))
        self.labelAlltimeScore.setText(_translate("mainWindow", "0 WPM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
