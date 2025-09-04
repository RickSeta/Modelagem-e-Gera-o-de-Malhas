import numpy as np
from PySide6 import QtOpenGLWidgets
from PySide6.QtWidgets import *
import matplotlib.pyplot as plt
from OpenGL.GL import *
import sys

class Canvas(QtOpenGLWidgets.QOpenGLWidget):

    def __init__(self):
        super(Canvas,self).__init__()
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("gldrawer")
        self.m_w = 0
        self.m_h = 0

    def initializeGL(self):
        glClearColor(0.0,0.0,0.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
    
    
    def resizeGL(self, w, h):
        self.m_w = w
        self.m_h = h
        glViewport(0, 0, self.m_w, self.m_h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1000.0,1000, -1000.0, 1000, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glShadeModel(GL_SMOOTH)


        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        glColor3f(1.0,1.0,1.0)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        glVertex2i(-1000, 0)
        glVertex2i(1000, 0)
        glVertex2i(0, -1000)
        glVertex2i(0, 1000)
        glEnd()

        glTranslatef(40.0, 40.0, 0.0)
        glRotatef(30.0,0.0,0.0,1.0)
        glScalef(2.0,2.0,0.0)

        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.0)
        glVertex2i(-20, -20)
        glVertex2i(20 , -20)
        glVertex2i(20 , 20)
        glVertex2i(-20, 20)
        glEnd()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget= Canvas()
    widget.show()
    sys.exit(app.exec())


