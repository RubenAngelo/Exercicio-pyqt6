import sys
import platform
from PyQt6 import uic
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap)
from PyQt6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt6.QtWidgets import *


def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText("")
    if dado_lido == '':
        QMessageBox.about(janela, "alerta", "Nenhum nome digitado")

    else:
        QMessageBox.about(janela, "alerta", dado_lido)


app = QtWidgets.QApplication([])
janela = uic.loadUi("4.ui")

# janela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
janela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

janela.pushButton.clicked.connect(exibir_mensagem)

janela.show()
app.exec()
