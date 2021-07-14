from PyQt5.QtWidgets import *
from PyQt5 import QtGui

from PyQt5.QtCore import *
import sys
from AnalizadorRUBY.sintactico import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 800, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets


    def UiComponents(self):
        rootPrincipal = QHBoxLayout()
        rootPrincipal.setAlignment(Qt.AlignTop)

        panelIzquierdo = QVBoxLayout()
        panelDerecho = QVBoxLayout()
        strAlgoritmo=algoritmo(self)
        self.label1=QLabel("Escriba su codigo",self)

        panelIzquierdo.addWidget(self.label1)


        self.texto = QPlainTextEdit(strAlgoritmo,self)
        self.texto.setMaximumWidth(400)
        panelIzquierdo.addWidget(self.texto)


        #----------------------------------------------
        self.rbtnLexico = QRadioButton("Lexico",self)
        self.rbtnSintactico = QRadioButton("Sintactico",self)
        self.rbtnSemantica = QRadioButton("Semantico",self)
        self.rbtnGroup = QButtonGroup()
        self.rbtnGroup.addButton(self.rbtnLexico)
        self.rbtnLexico.setChecked(True)
        self.rbtnGroup.addButton(self.rbtnSintactico)
        self.rbtnGroup.addButton(self.rbtnSemantica)

        boxBotones = QHBoxLayout()
        boxBotones.addWidget(self.rbtnLexico)
        boxBotones.addWidget(self.rbtnSintactico)
        boxBotones.addWidget(self.rbtnSemantica)
        panelDerecho.addLayout(boxBotones)

        rootPrincipal.addLayout(panelIzquierdo)
        rootPrincipal.addLayout(panelDerecho)
        self.setLayout(rootPrincipal)

        self.errores = QPlainTextEdit(self)
        self.errores.setMaximumWidth(400)
        panelDerecho.addWidget(self.errores)
        self.label2 = QLabel(" ",self)
        panelDerecho.addWidget(self.label2)

        self.buttonAn = QPushButton("Analisis",self)
        self.buttonAn.clicked.connect(self.on_button_clicked)
        panelDerecho.addWidget(self.buttonAn)

    def on_button_clicked(self):
        if(self.rbtnLexico.isChecked()):
            lexico(self)
        elif(self.rbtnSintactico.isChecked()):
            sintactico(self)
        elif(self.rbtnSemantica.isChecked()):
            semantico(self)
    # action method
from AnalizadorRUBY.AnalizadorRuby import *
import ply.lex as lex
def lexico(self):
    print("lexico")
    self.errores.clear()
    extraido=self.texto.toPlainText()

    listaTokens=leer(extraido)
    formateado=listaString(listaTokens)

    self.errores.setPlainText(formateado)


def sintactico(self):
    print("Sintactico")
    self.errores.clear()
    extraido=self.texto.toPlainText()

    strErrores=buildLSemantico(extraido)
    print(strErrores)
    if(strErrores[1]=="Error"):
        self.errores.setPlainText("Syntax error in input!")

    else:
        self.errores.setPlainText("None")

def semantico(self):
    print("Semantico")
    self.errores.clear()
    self.texto.clear()
    strDefault=algoritmoSemantico(self)
    self.texto.setPlainText(strDefault)
    extraido = self.texto.toPlainText()

    strErrores = buildLSemantico(extraido)
    print(strErrores)
    if (strErrores[1] == "Error"):
        self.errores.setPlainText("Syntax error in input!")

    else:
        self.errores.setPlainText("None")

def clickme(self):
    # printing pressed
    print("pressed")
def listaString(lista):
    salida=""
    for i in lista:

        salida=salida+str(i)+"\n"

    return salida

def algoritmoSemantico(self):
    strCodigo="""booleano=7>8 """
    return strCodigo
def algoritmo(self):
    strCodigo = """while(true) do
        puts hola
        end"""
    return strCodigo
# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


# def on_rbtn_clicked():
#     print("algo")
#
#     # parser = yacc.yacc()
#     #
#     # while True:
#     #     try:
#     #         s = input('calc > ')
#     #     except EOFError:
#     #         break
#     #     if not s: continue
#     #     result = parser.parse(s)
#     #     print(result)

# def on_button_clicked():
#
#     # alert = QMessageBox()
#     # alert.setText('You clicked the button!')
#     # alert.exec()
#
#     print("algo")


