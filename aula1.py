from PySide6.QtWidgets import *
from PySide6.QtCore import *
import numpy as np
import matplotlib.pyplot as plt
import sys


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.setGeometry(100,100,200,75)
        self.setWindowTitle("myy")
        self.r1 = QLabel("a = ")
        self.r2 = QLabel("b = ")
        self.r3 = QLabel("a + b = ")
        self.t1 = QLineEdit()
        self.t2 = QLineEdit()
        self.t3 = QLineEdit()
        self.b1 = QPushButton("Soma")
        self.b2 = QPushButton("Multiplicacao")
        self.b3 = QPushButton("Divisao")
        self.b4 = QPushButton("Subtracao")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.r1)
        self.vbox.addWidget(self.t1)
        self.vbox.addWidget(self.r2)
        self.vbox.addWidget(self.t2)
        self.vbox.addWidget(self.r3)
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)
        self.vbox.addWidget(self.t3)
        self.setLayout(self.vbox)

        self.b1.clicked.connect(self.soma)
        self.b2.clicked.connect(self.mult)
        self.b3.clicked.connect(self.div)
        self.b4.clicked.connect(self.sub)

    def soma(self):
        print("clicado")
        a = float(self.t1.text())
        b = float(self.t2.text())
        self.t3.setText(str(a+b))

    
    def mult(self):
        print("clicado")
        a = float(self.t1.text())
        b = float(self.t2.text())
        self.t3.setText(str(a*b))


    def div(self):
        print("clicado")
        a = float(self.t1.text())
        b = float(self.t2.text())
        self.t3.setText(str(a/b))


    def sub(self):
        print("clicado")
        a = float(self.t1.text())
        b = float(self.t2.text())
        self.t3.setText(str(a-b))



def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Ola mundo")

    b.setAlignment(Qt.AlignCenter)

    w.setGeometry(100,100,200,75)
    b.move(50,20)
    w.setWindowTitle("Xum")
    w.show()
    sys.exit(app.exec_())


app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
