# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1011, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 971, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(115, 570, 781, 102))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.connectBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout.addWidget(self.connectBtn, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.createAddressButton = QtWidgets.QPushButton(self.tab_4)
        self.createAddressButton.setGeometry(QtCore.QRect(10, 71, 117, 20))
        self.createAddressButton.setObjectName("createAddressButton")
        self.KeysDisplay = QtWidgets.QTextBrowser(self.tab_4)
        self.KeysDisplay.setGeometry(QtCore.QRect(10, 130, 751, 231))
        self.KeysDisplay.setObjectName("KeysDisplay")
        self.privateKeyInsert = QtWidgets.QLineEdit(self.tab_4)
        self.privateKeyInsert.setGeometry(QtCore.QRect(150, 70, 221, 20))
        self.privateKeyInsert.setText("")
        self.privateKeyInsert.setObjectName("privateKeyInsert")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(10, 40, 361, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 20, 251, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OP_PUSH = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OP_PUSH.setObjectName("OP_PUSH")
        self.gridLayout_2.addWidget(self.OP_PUSH, 0, 0, 1, 1)
        self.OP_EQUAL = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OP_EQUAL.setObjectName("OP_EQUAL")
        self.gridLayout_2.addWidget(self.OP_EQUAL, 3, 0, 1, 1)
        self.OP_DUP = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OP_DUP.setObjectName("OP_DUP")
        self.gridLayout_2.addWidget(self.OP_DUP, 1, 0, 1, 1)
        self.OP_HASH160 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OP_HASH160.setObjectName("OP_HASH160")
        self.gridLayout_2.addWidget(self.OP_HASH160, 2, 0, 1, 1)
        self.OP_VERIFY = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OP_VERIFY.setObjectName("OP_VERIFY")
        self.gridLayout_2.addWidget(self.OP_VERIFY, 4, 0, 1, 1)
        self.scriptText = QtWidgets.QTextBrowser(self.tab_5)
        self.scriptText.setGeometry(QtCore.QRect(70, 290, 791, 201))
        self.scriptText.setObjectName("scriptText")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(360, 20, 251, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.OP_RETURN = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.OP_RETURN.setObjectName("OP_RETURN")
        self.gridLayout_5.addWidget(self.OP_RETURN, 0, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_5.addWidget(self.pushButton_24, 3, 0, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_5.addWidget(self.pushButton_25, 1, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_5.addWidget(self.pushButton_26, 2, 0, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_5.addWidget(self.pushButton_27, 4, 0, 1, 1)
        self.scriptLine = QtWidgets.QTextBrowser(self.tab_5)
        self.scriptLine.setGeometry(QtCore.QRect(70, 250, 791, 31))
        self.scriptLine.setObjectName("scriptLine")
        self.clearBtn = QtWidgets.QPushButton(self.tab_5)
        self.clearBtn.setGeometry(QtCore.QRect(650, 30, 211, 161))
        self.clearBtn.setObjectName("clearBtn")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Pong"))
        self.pushButton_4.setText(_translate("MainWindow", "Ping"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.connectBtn.setText(_translate("MainWindow", "Conncect"))
        self.pushButton.setText(_translate("MainWindow", "Version"))
        self.pushButton_2.setText(_translate("MainWindow", "Verack"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Messages"))
        self.createAddressButton.setText(_translate("MainWindow", "Create Bitcoin Address"))
        self.label.setText(_translate("MainWindow", "Insert Private key or leave Empty to generate a random address and keys"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Keys"))
        self.OP_PUSH.setText(_translate("MainWindow", "OP_PUSH"))
        self.OP_EQUAL.setText(_translate("MainWindow", "OP_EQUAL"))
        self.OP_DUP.setText(_translate("MainWindow", "OP_DUP"))
        self.OP_HASH160.setText(_translate("MainWindow", "OP_HASH160"))
        self.OP_VERIFY.setText(_translate("MainWindow", "OP_VERIFY"))
        self.OP_RETURN.setText(_translate("MainWindow", "OP_RETURN    "))
        self.pushButton_24.setText(_translate("MainWindow", "soon"))
        self.pushButton_25.setText(_translate("MainWindow", "soon"))
        self.pushButton_26.setText(_translate("MainWindow", "soon"))
        self.pushButton_27.setText(_translate("MainWindow", "soon"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Scripts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))

