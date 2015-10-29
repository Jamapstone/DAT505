from graphics import *
import random
import time

# Do some simple drawing
window = GraphWin("Visualisation", 800, 800)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
lines = datafile.readlines()

#Ball Animation Code

xspeed = 25
yspeed = 75
ball = Circle(Point(100,100), 10)
ball.setFill(color_rgb(255,102,178))
ball.draw(window)

while True:
    for line in lines:
        time.sleep(0.25)
        ball.undraw()
        mark = float(line.strip());
        print(mark)
        currentPos = ball.getCenter()
        if(currentPos.getY() >= 800 - mark): yspeed = -yspeed
        if(currentPos.getY() <= 0 + mark): yspeed = -yspeed
        if(currentPos.getX() >= 800 - mark): xspeed = -xspeed
        if(currentPos.getX() <= 0 + mark): xspeed = -xspeed
        ball = Circle(Point(0,0), mark)
        ball.move(currentPos.getX()+xspeed,currentPos.getY()+yspeed) 
   
        if(mark >= 0.00) and (mark < 39.99): ball.setFill(color_rgb(204,0,0))
        if(mark >= 40.00) and (mark < 49.99): ball.setFill(color_rgb(255,102,178))
        if(mark >= 50.0) and (mark < 59.99): ball.setFill(color_rgb(255,153,51))
        if(mark >= 60.00) and (mark < 69.99): ball.setFill(color_rgb(255,255,102))
        if(mark >= 70.00) and (mark < 100.00): ball.setFill(color_rgb(76,153,0))
        ball.draw(window)
        time.sleep(0.25)

# Waits until the mouse is clicked before closing the window
window.getMouse()

