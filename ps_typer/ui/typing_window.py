# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source/typing_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_typingWindow(object):
    def setupUi(self, typingWindow):
        typingWindow.setObjectName("typingWindow")
        typingWindow.resize(830, 619)
        self.verticalLayout = QtWidgets.QVBoxLayout(typingWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(typingWindow)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 599))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(800, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineInput.sizePolicy().hasHeightForWidth())
        self.lineInput.setSizePolicy(sizePolicy)
        self.lineInput.setMinimumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaximumSize(QtCore.QSize(0, 0))
        self.lineInput.setMaxLength(100000)
        self.lineInput.setObjectName("lineInput")
        self.verticalLayout_2.addWidget(self.lineInput)
        spacerItem = QtWidgets.QSpacerItem(0, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelTitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.labelTitle.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("")
        self.labelTitle.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_2.addWidget(self.labelTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.labelMainText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMainText.sizePolicy().hasHeightForWidth())
        self.labelMainText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelMainText.setFont(font)
        self.labelMainText.setStyleSheet("padding: 0 100px; font-size: 26pt;")
        self.labelMainText.setLineWidth(1)
        self.labelMainText.setMidLineWidth(1)
        self.labelMainText.setTextFormat(QtCore.Qt.RichText)
        self.labelMainText.setScaledContents(False)
        self.labelMainText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMainText.setWordWrap(True)
        self.labelMainText.setIndent(-1)
        self.labelMainText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelMainText.setObjectName("labelMainText")
        self.verticalLayout_2.addWidget(self.labelMainText)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayoutButtons.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem3)
        self.buttonMainMenu = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMainMenu.sizePolicy().hasHeightForWidth())
        self.buttonMainMenu.setSizePolicy(sizePolicy)
        self.buttonMainMenu.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonMainMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonMainMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonMainMenu.setAutoDefault(False)
        self.buttonMainMenu.setDefault(False)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayoutButtons.addWidget(self.buttonMainMenu)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem4)
        self.buttonRestart = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRestart.sizePolicy().hasHeightForWidth())
        self.buttonRestart.setSizePolicy(sizePolicy)
        self.buttonRestart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonRestart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonRestart.setObjectName("buttonRestart")
        self.horizontalLayoutButtons.addWidget(self.buttonRestart)
        spacerItem5 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem5)
        self.buttonNewText = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewText.sizePolicy().hasHeightForWidth())
        self.buttonNewText.setSizePolicy(sizePolicy)
        self.buttonNewText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonNewText.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNewText.setObjectName("buttonNewText")
        self.horizontalLayoutButtons.addWidget(self.buttonNewText)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem6)
        self.labelTime = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTime.setObjectName("labelTime")
        self.horizontalLayoutButtons.addWidget(self.labelTime)
        self.labelUnit = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelUnit.setObjectName("labelUnit")
        self.horizontalLayoutButtons.addWidget(self.labelUnit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayoutButtons)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(typingWindow)
        QtCore.QMetaObject.connectSlotsByName(typingWindow)

    def retranslateUi(self, typingWindow):
        _translate = QtCore.QCoreApplication.translate
        typingWindow.setWindowTitle(_translate("typingWindow", "Typing window"))
        self.labelTitle.setText(_translate("typingWindow", "Mode"))
        self.labelMainText.setText(_translate("typingWindow", "Placeholder text: you should not be seeing this :("))
        self.buttonMainMenu.setText(_translate("typingWindow", "Back"))
        self.buttonRestart.setText(_translate("typingWindow", "Restart"))
        self.buttonNewText.setText(_translate("typingWindow", "New Text"))
        self.labelTime.setText(_translate("typingWindow", "1000"))
        self.labelUnit.setText(_translate("typingWindow", "s"))
