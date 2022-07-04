import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def somar():
    soma = 0
    if p_tela.checkBox_2.isChecked():
        soma += 15

    if p_tela.checkBox_4.isChecked():
        soma += 20

    if p_tela.checkBox_5.isChecked():
        soma += 10

    if p_tela.checkBox_3.isChecked():
        soma += 32

    if p_tela.checkBox.isChecked():
        soma += 5.50

    soma = f"R${soma:,.2f}"
    soma = soma.replace(".", ",")

    p_tela.label.setText(f"Valor total: {soma}")


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("9.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.pushButton.clicked.connect(somar)

p_tela.show()
app.exec()
