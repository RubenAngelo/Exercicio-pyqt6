import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

valor = 0


def mais_valor():
    global valor
    valor += 10
    p_tela.progressBar.setValue(valor)


def menos_valor():
    global valor
    valor = 0
    p_tela.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("6.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.pushButton.clicked.connect(mais_valor)
p_tela.pushButton_2.clicked.connect(menos_valor)

p_tela.show()
app.exec()
