from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WINDOW_SIZE=500
x=0
y=100
angle1=0
angle2=0
dir1=1
dir2=1
fps=120

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawMan():
	global x,y
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(100*math.cos(i*math.pi/180)+x,100*math.sin(i*math.pi/180)+y)
	glEnd()
	
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x-40,y+20)
	for i in range(0,361,1):
		glVertex2f(20*math.cos(i*math.pi/180)+x-40,20*math.sin(i*math.pi/180)+y+20)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x+40,y+20)
	for i in range(0,361,1):
		glVertex2f(20*math.cos(i*math.pi/180)+x+40,20*math.sin(i*math.pi/180)+y+20)
	glEnd()
	
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_TRIANGLES)
	glVertex2f(x,y)
	glVertex2f(x-20,y-20)
	glVertex2f(x+20,y-20)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(x-30,y-50)
	glVertex2f(x-30,y-70)
	glVertex2f(x+30,y-50)
	glVertex2f(x+30,y-70)
	glEnd()

	glColor3f(1.0,1.0,1.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y-250)
	for j in range(0,361,1):
		glVertex2f(150*math.cos(j*math.pi/180)+x,150*math.sin(j*math.pi/180)+y-250)
	glEnd()
	
	glLineWidth(10)
	glBegin(GL_LINES)
	glVertex2f(x+100,y-200)
	glVertex2f(300*math.cos(angle1*math.pi/180)+x,300*math.sin(angle1*math.pi/180)+y-100)
	glEnd()
	
	glLineWidth(10)
	glBegin(GL_LINES)
	glVertex2f(x-100,y-200)
	glVertex2f(-300*math.cos(angle2*math.pi/180)+x,-300*math.sin(angle2*math.pi/180)+y-100)
	glEnd()
	
	glutSwapBuffers()
	
def animate(temp):
	global dir1,dir2,angle1,angle2
	if dir1==1:
		angle1=angle1+1
		if angle1==45:
			dir1=0
	else:
		angle1=angle1-1
		if angle1==0:
			dir1=1
	if dir2==1:
		angle2=angle2-1
		if angle2==-45:
			dir2=0
	else:
		angle2=angle2+1
		if angle2==0:
			dir2=1
	glutPostRedisplay()
	glutTimerFunc(int(1000/fps),animate,0)
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Snow Man")
	glutDisplayFunc(drawMan)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawMan)
	init()
	glutMainLoop()
	
main()
