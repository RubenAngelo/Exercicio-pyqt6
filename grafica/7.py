import sys
import platform
from PyQt6 import uic, QtGui, QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


def pegar_data():
    data = str(p_tela.calendarWidget.selectedDate())
    data2 = data[19:len(data) - 1]
    data3 = data2.replace(" ", "").split(",")

    if int(data3[1]) > 9 and int(data3[2]) > 9:
        data4 = f"Data selecionada: {data3[2]}/{data3[1]}/{data3[0]}"
        p_tela.label.setText(data4)

    elif int(data3[1]) < 9 < int(data3[2]):
        data4 = f"Data selecionada: {data3[2]}/0{data3[1]}/{data3[0]}"
        p_tela.label.setText(data4)

    elif int(data3[1]) > 9 > int(data3[2]):
        data4 = f"Data selecionada: 0{data3[2]}/{data3[1]}/{data3[0]}"
        p_tela.label.setText(data4)

    elif int(data3[1]) < 9 and int(data3[2]) < 9:
        data4 = f"Data selecionada: 0{data3[2]}/0{data3[1]}/{data3[0]}"
        p_tela.label.setText(data4)


app = QtWidgets.QApplication([])
p_tela = uic.loadUi("7.ui")
# p_tela.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
p_tela.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

p_tela.calendarWidget.selectionChanged.connect(pegar_data)

p_tela.show()
app.exec()
