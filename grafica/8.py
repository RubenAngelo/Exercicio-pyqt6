import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def menu_verde():
    p_tela.label_2.setText("Verde")
    p_tela.label_2.setStyleSheet('font: 75 24pt "MS Shell Dlg 2";color: green;')


def menu_vermelho():
    p_tela.label_2.setText("Vermelho")
    p_tela.label_2.setStyleSheet('font: 75 24pt "MS Shell Dlg 2";color: red;')


def menu_azul():
    p_tela.label_2.setText("Azul")
    p_tela.label_2.setStyleSheet('font: 75 24pt "MS Shell Dlg 2";color: blue;')


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("8.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.actionverde.triggered.connect(menu_verde)
p_tela.actionvermelho.triggered.connect(menu_vermelho)
p_tela.actionazul.triggered.connect(menu_azul)

p_tela.show()
app.exec()
