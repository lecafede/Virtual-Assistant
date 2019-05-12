# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Python Developer\Desktop\Курсовая работа\Программа версии 2.0\interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 69)
        MainWindow.setMinimumSize(QtCore.QSize(231, 69))
        MainWindow.setMaximumSize(QtCore.QSize(231, 69))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius:25px;\n"
"color: white; /* цвет текста */\n"
"  text-decoration: none; /* убирать подчёркивание у ссылок */\n"
"  user-select: none; /* убирать выделение текста */\n"
"  background:rgb(212,75,56); /* фон кнопки */\n"
"  padding: .7em 1.5em; /* отступ от текста */\n"
"  outline: none; /* убирать контур в Mozilla */\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background:rgba(184, 52, 31, 1);;\n"
"\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../microphone-white-shape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(35, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 51, 51))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"border-radius:25px;\n"
"color: white; /* цвет текста */\n"
"  text-decoration: none; /* убирать подчёркивание у ссылок */\n"
"  user-select: none; /* убирать выделение текста */\n"
"  background:rgb(212,75,56); /* фон кнопки */\n"
"  padding: .7em 1.5em; /* отступ от текста */\n"
"  outline: none; /* убирать контур в Mozilla */\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background:rgba(184, 52, 31, 1);;\n"
"\n"
"}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../settings-gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 161))
        self.label.setMinimumSize(QtCore.QSize(411, 161))
        self.label.setMaximumSize(QtCore.QSize(411, 161))
        self.label.setStyleSheet("* {\n"
"font-family: Arial;\n"
"font-size: 24x\n"
"}\n"
"\n"
"QFrame{\n"
"background: #333;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Assistant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

