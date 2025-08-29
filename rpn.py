
class RPN():
  
  def __init__(self):
    self.pilha = []
    
  def addPilha(self, termo):
    self.pilha.append(termo)
  
  def soma(self):
    lastTerm = self.pilha.pop()
    secondToLastTerm = self.pilha.pop()
    self.pilha.append(int(lastTerm) + int(secondToLastTerm))
  
    
  def mult(self):
    lastTerm = self.pilha.pop()
    secondToLastTerm = self.pilha.pop()
    self.pilha.append(int(lastTerm) * int(secondToLastTerm))
  
    
  def div(self):
    lastTerm = self.pilha.pop()
    secondToLastTerm = self.pilha.pop()
    self.pilha.append(int(lastTerm) / int(secondToLastTerm))
  
    
  def sub(self):
    lastTerm = self.pilha.pop()
    secondToLastTerm = self.pilha.pop()
    self.pilha.append(int(lastTerm) - int(secondToLastTerm))