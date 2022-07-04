import sys
import platform
from PyQt6 import uic
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap)
from PyQt6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt6.QtWidgets import *

palavra = []


def listar_dados():
    palavra_re = []

    texto = lista.lineEdit.text().strip()
    texto_ver = texto.replace(" ", "")
    palavra_re.append(texto_ver)

    if "" in palavra_re:
        pass

    else:
        palavra.append(texto)
        lista.listWidget.addItem(texto)

        print(palavra)

    lista.lineEdit.setText("")


def deletar():
    lista.listWidget.clear()


app = QtWidgets.QApplication([])
lista = uic.loadUi("3.ui")

lista.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
lista.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

lista.pushButton.clicked.connect(listar_dados)
lista.pushButton_2.clicked.connect(deletar)

lista.show()
app.exec()
