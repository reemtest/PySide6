# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1075, 654)
        self.textLabel = QLabel(Form)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setGeometry(QRect(420, 270, 131, 51))
        font = QFont()
        font.setPointSize(23)
        self.textLabel.setFont(font)
        self.changeButton = QPushButton(Form)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setGeometry(QRect(540, 270, 121, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(148, 160, 201, 81))
        self.label.setPixmap(QPixmap(u"/photo/net.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(750, 170, 49, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.textLabel.setText(QCoreApplication.translate("Form", u"Text", None))
        self.changeButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/photo/net.png", None))
    # retranslateUi

