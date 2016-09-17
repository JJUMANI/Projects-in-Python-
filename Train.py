#  File: Train.py

#  Description: Draw Train

#  Student's Name:Junaid K. Jumani

#  Student's UT EID: jkj696
 
#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 27th 2016

#  Date Last Modified: February 29th 2016

import turtle, math
#Draw Circle
def circle (tt1, x, y, radius, angle):
	tt1.color ('red')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.circle (radius, angle)
#Draw left side of train
def Drawline (tt1, x, y, size, angle):
	tt1.color ('blue')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.forward(20)
	tt1.left(angle)
	tt1.forward(size)
	tt1.left(angle)
	tt1.forward(size-50)
	tt1.left(angle)
	tt1.forward(size)
	tt1.left(angle)
	tt1.forward(20)
	tt1.left(angle)
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.circle (30, 180)
	tt1.penup()
	tt1.goto (x - 50, y)
	tt1.pendown()
	tt1.color ('red')
	tt1.circle (20, 360)
	tt1.penup()
	tt1.goto (x - 45, y)
	tt1.pendown()
	tt1.circle (15, 360)
	tt1.penup()
	tt1.goto (x - 35, y)
	tt1.pendown()
	tt1.circle (5, 360)
#Draw Right Side of Train
def Drawline2 (tt1, x, y, size, angle):
	tt1.color ('blue')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.left(angle)	
	tt1.forward(30)
	tt1.right(45)
	tt1.forward(30)
	tt1.right(135)
	tt1.forward(45)
	tt1.right(angle)
	tt1.forward(size+40)
	tt1.left(angle)
	tt1.forward(size+75)
	tt1.left(angle)
	tt1.forward(size+30)
	tt1.left(angle)
	for semicircle in range (2):
		tt1.forward(size/3)
		tt1.right(angle)
		tt1.circle(20, -180)
		tt1.right(angle)
	tt1.forward(size/3)
	tt1.penup()
#Draw Squares of train
def Drawsquare (tt1, x, y, side, angle):
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	for i in range (4):
		tt1.forward(side)
		tt1.left(angle)
		tt1.forward(side)
	tt1.penup()	
def Drawline3 (tt1, x, y, size, angle):
	tt1.color ('blue')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.forward(20)
	tt1.left(angle)
	tt1.forward(5)
	tt1.left(angle)
	tt1.forward(20+size+20)
	tt1.left(angle)
	tt1.forward(5)
	tt1.left(angle)
	tt1.forward(20)
	tt1.penup()
def Drawline4 (tt1, x, y, size, angle):
	tt1.color ('blue')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.left(angle)
	tt1.forward(10)
	tt1.left(angle)
	tt1.forward(size)
	tt1.left(angle)
	tt1.forward(10)
	tt1.right(angle)
	tt1.right(angle)
	tt1.forward(10)
	tt1.right(angle)
	tt1.forward(size/4)
	tt1.left(angle)
	tt1.forward(5)
	tt1.right(angle)
	tt1.forward(size/2)
	tt1.right(angle)
	tt1.forward(5)
	tt1.pendown()
def DrawPent (tt1, x, y, size):
	tt1.color('blue')
	tt1.penup()
	tt1.goto(x, y)
	tt1.pendown()
	tt1.left(180)
	tt1.left(180)
	tt1.left(125)
	tt1.forward(size)
	tt1.right(75)
	tt1.forward(size/3)
	tt1.right(50)
	tt1.forward(size)
	tt1.right(50)
	tt1.forward(size/3)
	tt1.right(75)
	tt1.forward(size)
	tt1.right(180)
	tt1.forward(size)
	tt1.left(125)
	tt1.forward(size+size/2)
	
	
def DrawSingleline(tt1, x, y, size, angle):
	tt1.color ('black')
	tt1.penup()
	tt1.goto (x, y)
	tt1.pendown()
	tt1.right(180)
	tt1.forward(size)
	tt1.penup()
	tt1.right(angle)
	tt1.forward(5)
	tt1.right(angle)
	tt1.pendown()
	tt1.forward(size)
	tt1.left(180)
	for square in range(13):
		tt1.forward(size/26)
		tt1.right(angle)
		tt1.forward(5)
		tt1.left(angle)
		tt1.forward(size/26)
		tt1.left(angle)
		tt1.forward(5)
		tt1.right(angle)
	tt1.penup()	
def spokes(tt1, x, y, size, small_size):
	tt1.color('red')
	tt1.penup()
	tt1.goto(x, y)
	tt1.pendown()
	for i in range(8):
	   tt1.penup()
	   tt1.forward(small_size)
	   tt1.pendown()	   
	   tt1.forward(size-small_size)
	   tt1.right(180)
	   tt1.forward(size-small_size)
	   tt1.penup()
	   tt1.forward(small_size)
	   tt1.right(180)
	   tt1.right(10)
	   tt1.forward(small_size)
	   tt1.pendown()
	   tt1.forward(size-small_size)
	   tt1.right(180)
	   tt1.forward(size-small_size)
	   tt1.penup()
	   tt1.forward(small_size)
	   tt1.right(180)
	   tt1.right(35)
	   
def main():	
	turtle.title('Train')
	turtle.setup(800, 800, 0, 0)
	tt1 = turtle.Turtle()
	Drawline (tt1, 0, 0, 150, 90)
	tt1.fillcolor ('gray')
	tt1.begin_fill()
	Drawsquare (tt1, -60, 100, 15, 90)
	tt1.end_fill()
	tt1.fillcolor ('gray')
	tt1.begin_fill()
	Drawsquare (tt1, -20, 100, 15, 90)
	tt1.end_fill()
	Drawline2 (tt1, 190, 11, 100, 90)
	circle (tt1, 75, -20, 15, 360)
	circle (tt1, 75, -15, 10, 360)
	circle (tt1, 75, -7, 2, 360)
	circle (tt1, 147, -20, 15, 360)
	circle (tt1, 147, -15, 10, 360)
	circle (tt1, 147, -7, 2, 360)
	Drawline3 (tt1, 20, 150, 100, 90)
	Drawline4 (tt1, (100/3)+40+20, 130, 20, 90)
	Drawline4 (tt1, 195, 20, 90, 90)
	DrawSingleline(tt1, -90, -20, 375, 90)
	spokes(tt1, -30, 0, 15, 5)
	spokes(tt1, 147, -5, 10, 2)
	spokes(tt1, 75, -5, 10, 2)
	DrawPent (tt1, 20+(200/3)+60, 130, 35)
	turtle.done()
main()