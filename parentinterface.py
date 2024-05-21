# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1271, 796)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 161, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 0, 221, 31))
        self.label_2.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 30, 621, 681))
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(640, 30, 621, 681))
        self.plainTextEdit_2.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 740, 421, 41))
        self.pushButton.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 740, 191, 41))
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(6)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 710, 181, 31))
        self.label_3.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(640, 740, 621, 41))
        self.pushButton_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u044e\u0434\u0430 \u043d\u0443\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u0442\u0435\u043a\u0441\u0442...", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u043b\u0438\u043c\u043e\u043d\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447(6 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0434\u043b\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u043d\u043e\u0433\u043e \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
    # retranslateUi

