import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def chama_segunda_tela():
    s_tela.show()


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("5.ui")
s_tela = uic.loadUi("5.1.ui")

# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

# s_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
s_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.pushButton.clicked.connect(chama_segunda_tela)

p_tela.show()
app.exec()
