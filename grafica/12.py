import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def salvar():
    nome = p_tela.lineEdit_4.text()
    idade = p_tela.lineEdit_5.text()
    tel = p_tela.lineEdit_6.text()

    dados = f'Nome: {nome} Idade: {idade} Telefone: {tel}'

    arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

    with open(f"{arquivo}.txt", "w") as alou:
        alou.write(dados)

    print(arquivo)


def ler_arquivo():
    arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]

    with open(arquivo, "r") as alou:
        p_tela.label_2.setText(alou.read())


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("12.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.actionSalvar.triggered.connect(salvar)
p_tela.actionAbrir.triggered.connect(ler_arquivo)

p_tela.show()
app.exec()
