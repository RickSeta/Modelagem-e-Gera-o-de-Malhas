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
        self.setWindowTitle("RPN Henrique")
        self.r1 = QLabel("Termo a ser adicionado")
        self.t1 = QLineEdit()
        self.r2 = QLabel("RPN")
        self.t2 = QLineEdit()
        self.appendB = QPushButton("Adicionar")
        self.b1 = QPushButton("Soma")
        self.b2 = QPushButton("Multiplicacao")
        self.b3 = QPushButton("Divisao")
        self.b4 = QPushButton("Subtracao")
        self.b5 = QPushButton("limpa")
        self.b6 = QPushButton("<")
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
        self.vbox.addWidget(self.b5)
        self.vbox.addWidget(self.b6)
        self.vbox.addWidget(self.exec)
        self.setLayout(self.vbox)

        self.b1.clicked.connect((lambda x: self.addOp(" + ")))
        self.b2.clicked.connect((lambda x: self.addOp(" * ")))
        self.b3.clicked.connect((lambda x: self.addOp(" / ")))
        self.b4.clicked.connect((lambda x: self.addOp(" - ")))
        self.b5.clicked.connect((lambda x: self.clear()))
        self.b6.clicked.connect((lambda x: self.back()))
        self.appendB.clicked.connect(self.addPilha)
        self.exec.clicked.connect(self.execute)

    def updateT2(self):
        self.t2.setText(" ".join(list(map(str,self.pilha))))

    def clear(self):
        self.pilha.clear()
        self.updateT2()

    def back(self):
        self.pilha.pop()
        self.updateT2()
    
    def addOp(self, op):
        self.pilha.append(op.strip(" "))
        self.updateT2()
        
    def parser(self):
        text = self.t1.text()
        temp = ""
        for x in range(len(text)):
            isOp = self.checkOp(text[x])
            if(text[x] == " " or isOp):
                if len(temp) > 0:
                   self.pilha.append(temp)
                temp = ""
                if isOp:
                    self.pilha.append(text[x])
            else:
                temp += text[x]

    def addPilha(self):
        print(self.t1.text())
        if not self.t1.text():
            return
        if(len(self.t1.text()) > 1):
            self.parser()
        else:
            self.pilha.append(self.t1.text())
        self.t1.setText("")
        self.updateT2()
        print(self.pilha)
  
    def soma(self):
        lastTerm = self.pilha.pop()
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
            print(self.pilha[-1])
            return
        if(self.checkOp(self.pilha[-1])):
            op = self.pilha.pop()

        lastTerm = self.pilha[-1]
        secondToLastTerm = self.pilha[-2]
        
        if self.checkOp(secondToLastTerm):
            temp = self.pilha.pop()
            self.execute()
            self.pilha.append(temp)
        if self.checkOp(lastTerm):
            self.execute()

        if(op == "+"):
            self.soma()        
        if(op == "-"):
            self.sub()        
        if(op == "/"):
            self.div()        
        if(op == "*"):
            self.mult() 
    
    def checkOp(self,op):
        return op in ["+", "-", "*", "/"]

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
