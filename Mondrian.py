#  File: Mondrian.py

#  Description: Draw Recusrsive Squares

#  Student's Name:Junaid K. Jumani

#  Student's UT EID: jkj696
 
#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 6th 2016

#  Date Last Modified: March 6th 2016

import turtle

# draw a square
def DrawSingleline(ttl, x, y, size, angle):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for i in range (4):
    ttl.forward(size)
    ttl.left(angle)
    ttl.forward(size)

# draw gasket recursively
def draw_gasket (ttl, level, x, y, size, angle):
  DrawSingleline(ttl, x, y, size, angle)
  if (level > 0):
  
    # recursively draw the other squares
    draw_gasket (ttl, level - 1, x - 50, y - 50, size, angle)


def main():
  # prompt the user to enter an level for the recursive squares
  level = int (input ('Enter a level of recursion between 1 and 6: '))
  while (level < 1 or level > 6):
    level = int (input ('Enter a level of recursion between 1 and 6: '))
  # put label on top of page
  turtle.title ('Recursive squares')
  # setup screen size
  turtle.setup (800, 800, 0, 0)
  # create a turtle object
  ttl = turtle.Turtle()
  # assign a color to the turtle object
  ttl.color ('navy')
  # draw the gasket
  draw_gasket (ttl, level, 125, 125, 120, 90)
  # persist drawing
  turtle.done()


main()