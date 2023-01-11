from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

sys.setrecursionlimit(10000)
window_size=700
point_size=3

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	
def get_pixel(x,y):
	pixel=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None)
	return pixel[0][0]
	
def set_pixel(x,y,fill_color):
	glColor3f(*fill_color)
	glPointSize(point_size)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	
def rectangle(vertices,color):
	glColor3f(color[0],color[1],color[2])
	glBegin(GL_POLYGON)
	for vertex in vertices:
		glVertex2f(*vertex)
	glEnd()
	
def plot_rect():
	glClear(GL_COLOR_BUFFER_BIT)
	gluOrtho2D(0,window_size,0,window_size)
	rectangle([[200,200],[200,400],[400,400],[400,200]],[1,0,0])
	glFlush()
	
def flood_fill(x,y,new_color,old_color):
	color=get_pixel(x,y)
	if all(color==old_color):
		set_pixel(x,y,new_color)
		flood_fill(x+point_size,y,new_color,old_color)
		flood_fill(x-point_size,y,new_color,old_color)
		flood_fill(x,y+point_size,new_color,old_color)
		flood_fill(x,y-point_size,new_color,old_color)
		
def mouse_click(button,state,x,y):
	y=window_size-y
	if button==GLUT_LEFT_BUTTON and state==GLUT_UP:
		flood_fill(x,y,[0,1,1],get_pixel(x,y))
		
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutCreateWindow("Flood Filling")
	glutDisplayFunc(plot_rect)
	glutMouseFunc(mouse_click)
	glutMainLoop()
	
main()
