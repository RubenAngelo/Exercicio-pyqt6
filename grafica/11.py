import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def opcao():
    cidade = p_tela.comboBox.currentText()

    p_tela.label_2.setText(f"Cidade: {cidade}")


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("11.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.pushButton.clicked.connect(opcao)

p_tela.comboBox.addItems(["São paulo", "Rio de janeiro"])


p_tela.show()
app.exec()
