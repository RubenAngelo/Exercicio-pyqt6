from PyQt6 import uic, QtWidgets


def funcao_principal():
    if formulario.radioButton_6.isChecked():
        opcao = "opção 1"
        formulario.label_2.setText(f"Cor selecionada: {opcao}")

    elif formulario.radioButton_4.isChecked():
        opcao = "opção 2"
        formulario.label_2.setText(f"Cor selecionada: {opcao}")

    elif formulario.radioButton_5.isChecked():
        opcao = "opção 3"
        formulario.label_2.setText(f"Cor selecionada: {opcao}")

    elif formulario.radioButton_3.isChecked():
        opcao = "opção 4"
        formulario.label_2.setText(f"Cor selecionada: {opcao}")

    else:
        opcao = ""
        formulario.label_2.setText(f"Cor selecionada: {opcao}")


app = QtWidgets.QApplication([])
formulario = uic.loadUi("projeto.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
