from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-100, 100.0, -100, 100.0)
	
def plotaxes():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_LINES)
	glVertex2f(0, -500)
	glVertex2f(0, 500)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(500, 0)
	glVertex2f(-500, 0)
	glEnd()
	
def plotgrid():
	glColor3f(0.202, 0.202, 0.202)
	for i in range(-500, 500, 50):
		if i != 0:
			glBegin(GL_LINES)
			glVertex2f(i, 500)
			glVertex2f(i, -500)
			glEnd()
			glBegin(GL_LINES)
			glVertex2f(500, i)
			glVertex2f(-500, i)
			glEnd()
			
def plotTraingle(x1, x2, x3, y1, y2, y3):
	glBegin(GL_LINES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x2, y2)
	glVertex2f(x3, y3)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(x3, y3)
	glVertex2f(x1, y1)
	glEnd()
	
def translate(x1, x2, x3, y1, y2, y3, tx, ty):
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D-Transformations - Translation")
	glutDisplayFunc(lambda: drawTranslated(x1, x2, x3, y1, y2, y3, tx, ty))
	init()
	glutMainLoop()
	
def drawTranslated(x1, x2, x3, y1, y2, y3, tx, ty):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([point[0]+tx, point[1]+ty])
	print(newpoints)
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTraingle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2][0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
	glFlush()
	
def rotateHelper(x, y, theta):
	return [round((x*math.cos(theta)) - (y*math.sin(theta))), round((x*math.sin(theta)) +(y*math.cos(theta)))]

def rotateAboutPoint(x1, x2, x3, y1, y2, y3):
	theta = (math.pi/180) * int(input("\nEnter the Degress to be Rotated: "))
	px = int(input("X Co-ordinate of Point: "))
	py = int(input("Y Co-ordinate of Point: "))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D-Transformations - Rotation About a Point")
	glutDisplayFunc(lambda: drawRotatedAboutPoint(x1, x2, x3, y1, y2, y3, theta, px, py))
	init()
	glutMainLoop()
	
def drawRotatedAboutPoint(x1, x2, x3, y1, y2, y3, theta, px, py):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append(rotateHelper(point[0] - px, point[1] - py, theta))
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTraingle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTraingle(newpoints[0][0] + px, newpoints[1][0] + px, newpoints[2][0] + px, newpoints[0][1] + py, newpoints[1][1] + py, newpoints[2][1] + py)
	glFlush()

def scaleAboutPoint(x1, x2, x3, y1, y2, y3):
	tx = int(input("\nEnter Scale Along X: "))
	ty = int(input("\nEnter Scale Along Y: "))
	px = int(input("X Co-ordinate of Point: "))
	py = int(input("Y Co-ordinate of Point: "))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("2D-Transformations - Scaling About a Point")
	glutDisplayFunc(lambda: drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py))
	init()
	glutMainLoop()
	
def drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py):
	points = [[x1, y1], [x2, y2], [x3, y3]]
	newpoints = []
	for point in points:
		newpoints.append([(point[0] - px)*tx, (point[1] - py)*ty])
	plotaxes()
	plotgrid()
	glColor3f(0, 0, 1)
	plotTraingle(x1, x2, x3, y1, y2, y3)
	glColor3f(1, 0, 1)
	plotTraingle(newpoints[0][0] + px, newpoints[1][0] + px, newpoints[2][0] + px, newpoints[0][1] + py, newpoints[1][1] + py, newpoints[2][1] + py)
	glFlush()
	
def main():
	print("\nEnter the Co-ordinates of Triangle: ")
	x1 = float(input("\n\tx1: "))
	y1 = float(input("\n\ty1: "))
	side = float(input("\n\tSide: "))
	x2 = x1 + side
	y2 = y1
	x3 = x1+side/2
	y3 = y1+0.86602540378*side
	print("\nChoose Transformations:\n\t1.Translation\n\t2.Rotation around a point\n\t3.Scaling about a point")
	ch = int(input("\nYour Choice: "))
	if ch == 1:
		translationX = int(input("\nX translation: "))
		translationY = int(input("\nY translation: "))
		translate(x1, x2, x3, y1, y2, y3, translationX, translationY)
	elif ch == 2:
		rotateAboutPoint(x1, x2, x3, y1, y2, y3)
	elif ch == 3:
		scaleAboutPoint(x1, x2, x3, y1, y2, y3)
main()
