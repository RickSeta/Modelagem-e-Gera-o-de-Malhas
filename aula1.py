from PySide6.QtWidgets import *
from PySide6.QtCore import *
import numpy as np
import matplotlib.pyplot as plt
import sys
from rpn import RPN


class MyWidget(QWidget, RPN):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.pilha = []
        self.setGeometry(100,100,200,75)
        self.setWindowTitle("myy")
        self.r1 = QLabel("Termo a ser adicionado")
        self.t1 = QLineEdit()
        self.r2 = QLabel("RPN")
        self.t2 = QLineEdit()
        self.appendB = QPushButton("Adicionar")
        self.b1 = QPushButton("Soma")
        self.b2 = QPushButton("Multiplicacao")
        self.b3 = QPushButton("Divisao")
        self.b4 = QPushButton("Subtracao")
        self.exec = QPushButton("Executar")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.r1)
        self.vbox.addWidget(self.t1)
        self.vbox.addWidget(self.r2)
        self.vbox.addWidget(self.appendB)
        self.vbox.addWidget(self.t2)
        
        
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)
        self.vbox.addWidget(self.exec)
        self.setLayout(self.vbox)

        self.b1.clicked.connect((lambda x: self.addOp("+")))
        self.b2.clicked.connect((lambda x: self.addOp("*")))
        self.b3.clicked.connect((lambda x: self.addOp("/")))
        self.b4.clicked.connect((lambda x: self.addOp("-")))
        self.appendB.clicked.connect(self.addPilha)
        self.exec.clicked.connect(self.execute)

    def updateT2(self):
        self.t2.setText(" ".join(list(map(str,self.pilha))))
    
    def addOp(self, op):
        self.pilha.append(op)
        self.updateT2()
        
        
    def addPilha(self):
        print(self.t1.text)
        self.pilha.append(self.t1.text())
        self.t1.setText("")
        self.updateT2()
        print(self.pilha)
  
    def soma(self):
        lastTerm = self.pilha.pop()
        if self.checkOp(lastTerm):
            self.execute()
            lastTerm = self.pilha.pop()
        secondToLastTerm = self.pilha.pop()
        if self.checkOp(secondToLastTerm):
            self.execute()
            secondToLastTerm = self.pilha.pop()
        self.pilha.append(int(lastTerm) + int(secondToLastTerm))
        
        self.updateT2()
    
        
    def mult(self):
        lastTerm = self.pilha.pop()
        secondToLastTerm = self.pilha.pop()
        self.pilha.append(int(lastTerm) * int(secondToLastTerm))
        self.updateT2()
    
        
    def div(self):
        secondToLastTerm = self.pilha.pop()
        lastTerm = self.pilha.pop()
        self.pilha.append(int(lastTerm) / int(secondToLastTerm))
        self.updateT2()
    
        
    def sub(self):
        secondToLastTerm = self.pilha.pop()
        lastTerm = self.pilha.pop()
        self.pilha.append(int(lastTerm) - int(secondToLastTerm))
        self.updateT2()
    
    def execute(self):
        
        if(len(self.pilha) < 3):
            print("fim")
            return
        op = self.pilha[-1]
        
        if(op == "+"):
            self.pilha.pop()
            self.soma()        
        if(op == "-"):
            self.pilha.pop()
            self.sub()        
        if(op == "/"):
            self.pilha.pop()
            self.div()        
        if(op == "*"):
            self.pilha.pop()
            self.mult()
    
    def checkOp(self,op):
        return op in ["+", "-", "*", "/"]
    # def soma(self):
    #     print("clicado")
    #     a = float(self.t1.text())
    #     b = float(self.t2.text())
    #     self.t3.setText(str(a+b))

    
    # def mult(self):
    #     print("clicado")
    #     a = float(self.t1.text())
    #     b = float(self.t2.text())
    #     self.t3.setText(str(a*b))


    # def div(self):
    #     print("clicado")
    #     a = float(self.t1.text())
    #     b = float(self.t2.text())
    #     self.t3.setText(str(a/b))


    # def sub(self):
    #     print("clicado")
    #     a = float(self.t1.text())
    #     b = float(self.t2.text())
    #     self.t3.setText(str(a-b))



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
