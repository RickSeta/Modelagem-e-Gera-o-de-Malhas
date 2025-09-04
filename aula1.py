from PySide6.QtWidgets import *
from PySide6.QtCore import *
import numpy as np
import matplotlib.pyplot as plt
import sys
from rpn import RPN
class MyWidget(QWidget, RPN):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("RPN Henrique")

        self.r1 = QLabel("Termo a ser adicionado")
        
        help_button = QToolButton()
        help_button.setText("?")
        help_button.setToolTip("Digite o número ou expressão a ser adicionada na pilha.")

        self.t1 = QLineEdit()
        self.r2 = QLabel("RPN")
        self.t2 = QLineEdit()
        self.t2.setReadOnly(True)

        self.appendB = QPushButton("Adicionar")
        self.b1 = QPushButton("+")
        self.b2 = QPushButton("*")
        self.b3 = QPushButton("/")
        self.b4 = QPushButton("-")
        self.b5 = QPushButton("Limpa")
        self.b6 = QPushButton("<")
        self.exec = QPushButton("Executar")

        self.vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.r1)
        hbox.addWidget(help_button)
        hbox.addStretch()
        self.vbox.addLayout(hbox)
        self.vbox.addWidget(self.t1)
        self.vbox.addWidget(self.appendB)
        self.vbox.addWidget(self.r2)
        self.vbox.addWidget(self.t2)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.b1)
        hbox1.addWidget(self.b2)
        self.vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.b3)
        hbox2.addWidget(self.b4)
        self.vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.b5)
        hbox3.addWidget(self.b6)
        self.vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        hbox4.addStretch()
        hbox4.addWidget(self.exec)
        hbox4.addStretch()
        self.vbox.addLayout(hbox4)

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
        text += (" ")
        temp = ""
        for x in (text):
            print(text)
            print(x)
            isOp = self.checkOp(x)
            print(isOp)
            if(x == " " or isOp):
                if len(temp) > 0:
                   print("temp ",temp)
                   self.pilha.append(temp)
                temp = ""
                if isOp:
                    self.pilha.append(x)
            else:
                temp += x

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
