import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def frame1():
    p_tela.frame_2.close()


def frame2():
    p_tela.frame_2.show()


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("10.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.pushButton_2.clicked.connect(frame1)
p_tela.pushButton_3.clicked.connect(frame2)

p_tela.show()
app.exec()
