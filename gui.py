from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from AnalizadorRUBY.sintactico import *


def __init__(self):
    super().__init__()

    # setting title
    self.setWindowTitle("Python ")

    # setting geometry
    self.setGeometry(100, 100, 600, 400)

    # calling method
    self.UiComponents()

    # showing all the widgets
    self.show()

# method for widgets
def UiComponents(self):
    # creating a push button
    button = QPushButton("CLICK", self)

    # setting geometry of button
    button.setGeometry(200, 150, 100, 30)

    # adding action to a button
    button.clicked.connect(self.clickme)

def window():
    app = QApplication([])
    win=QWidget()
    win.setGeometry(200,100,800,600)
    win.setWindowTitle("Analizador Ruby")

    rootPrincipal = QHBoxLayout()
    rootPrincipal.setAlignment(Qt.AlignTop)

    panelIzquierdo=QVBoxLayout()
    panelDerecho=QVBoxLayout()


    label1=QLabel("Escriba su codigo")
    # buttonIz=QPushButton("Izquierda")


    texto=QPlainTextEdit("Defecto")
    texto.setMaximumWidth(400)



    panelIzquierdo.addWidget(label1)

    panelIzquierdo.addWidget(texto)
    # separacion


    rbtnLexico=QRadioButton("Lexico")
    rbtnSintactico=QRadioButton("Sintactico")
    rbtnSemantica=QRadioButton("Semantico")
    rbtnGroup=QButtonGroup()
    rbtnGroup.addButton(rbtnLexico)
    rbtnLexico.setChecked(True)
    rbtnGroup.addButton(rbtnSintactico)
    rbtnGroup.addButton(rbtnSemantica)

    rbtnLexico.clicked.connect(on_rbtn_clicked)

    boxBotones=QHBoxLayout()
    boxBotones.addWidget(rbtnLexico)
    boxBotones.addWidget(rbtnSintactico)
    boxBotones.addWidget(rbtnSemantica)
    panelDerecho.addLayout(boxBotones)

    errores=QPlainTextEdit()
    errores.setMaximumWidth(400)
    panelDerecho.addWidget(errores)
    label2=QLabel(" ")
    panelDerecho.addWidget(label2)

    button = QPushButton("Analisis")
    button.clicked.connect(on_button_clicked)
    panelDerecho.addWidget(button)

    rootPrincipal.addLayout(panelIzquierdo)
    rootPrincipal.addLayout(panelDerecho)
    win.setLayout(rootPrincipal)

    win.show()
    sys.exit(app.exec_())
def on_rbtn_clicked():
    print("algo")

    # parser = yacc.yacc()
    #
    # while True:
    #     try:
    #         s = input('calc > ')
    #     except EOFError:
    #         break
    #     if not s: continue
    #     result = parser.parse(s)
    #     print(result)
tipoAnalisis="lexico"
def on_button_clicked():

    # alert = QMessageBox()
    # alert.setText('You clicked the button!')
    # alert.exec()

    print("algo")
