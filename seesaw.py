from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WINDOW_SIZE=500
MODE=1
ANGLE=0
X=0
Y=0
FPS=60

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawSeesaw():
	global X,Y
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_TRIANGLES)
	glVertex2f(X,Y)
	glVertex2f(X-30,Y-40)
	glVertex2f(X+30,Y-40)
	glEnd()

	glColor3f(1.0,1.0,1.0)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(X,Y)
	glVertex2f(150*math.cos(math.pi*ANGLE/180)+X,150*math.sin(math.pi*ANGLE/180)+Y)
	glEnd()	
	
	glColor3f(1.0,1.0,1.0)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(X,Y)
	glVertex2f(-150*math.cos(math.pi*ANGLE/180)+X,-150*math.sin(math.pi*ANGLE/180)+Y)
	glEnd()	
	
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_POLYGON)
	glVertex2f(150*math.cos(math.pi*ANGLE/180)+X,150*math.sin(math.pi*ANGLE/180)+Y)
	glVertex2f(150*math.cos(math.pi*ANGLE/180)+X-40,150*math.sin(math.pi*ANGLE/180)+Y)
	glVertex2f(150*math.cos(math.pi*ANGLE/180)+X-40,150*math.sin(math.pi*ANGLE/180)+Y+40)
	glVertex2f(150*math.cos(math.pi*ANGLE/180)+X,150*math.sin(math.pi*ANGLE/180)+Y+40)
	glEnd()
	
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_POLYGON)
	glVertex2f(-150*math.cos(math.pi*ANGLE/180)+X,-150*math.sin(math.pi*ANGLE/180)+Y)
	glVertex2f(-150*math.cos(math.pi*ANGLE/180)+X+40,-150*math.sin(math.pi*ANGLE/180)+Y)
	glVertex2f(-150*math.cos(math.pi*ANGLE/180)+X+40,-150*math.sin(math.pi*ANGLE/180)+Y+40)
	glVertex2f(-150*math.cos(math.pi*ANGLE/180)+X,-150*math.sin(math.pi*ANGLE/180)+Y+40)
	glEnd()
	
	glutSwapBuffers()
	
def animate(temp):
	global ANGLE,MODE
	if MODE==1:
		ANGLE+=1
		if ANGLE==15:
			MODE=0
	elif MODE==0:
		ANGLE-=1
		if ANGLE==-15:
			MODE=1
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS),animate,0)
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Seesaw")
	glutDisplayFunc(drawSeesaw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawSeesaw)
	
	init()
	glutMainLoop()
	
main()
