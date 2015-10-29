from graphics import *
import random
import time

# Do some simple drawing
window = GraphWin("Visualisation", 800, 800)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
lines = datafile.readlines()


for line in lines:
    xpos = random.randint(50,750)
    ypos = random.randint(50,750)
    mark = float(line.strip());
    ball = Circle(Point(xpos,ypos), mark)
    time.sleep(1)
    ball.setFill(color_rgb(204,153,255))
    ball.draw(window)
    
    



# Waits until the mouse is clicked before closing the window
window.getMouse()