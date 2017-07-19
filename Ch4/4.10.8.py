#4.10.8.py
# This program allows the user to draw a line segment and then displays some graphical information about the line Segment

# import libraries
from graphics import *
from math import sqrt

def main():
    win = GraphWin("Line Segment Information",400, 400)
    for i in range(1):
        p1 = win.getMouse()
        p2 = win.getMouse()

    # variables needed
    dx = p2.getX()-p1.getX()
    dy = p2.getY()-p1.getY()
    m = dy/dx
    midX = (p1.getX()+p2.getX())/2
    midY = (p1.getY()+p2.getY())/2
    lineLength = sqrt((dx**2)+(dy**2))
    #lines and shapes
    line = Line(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
    line.setFill("black")
    line.draw(win)
    midPoint=Circle(Point(midX,midY),2)
    midPoint.setFill("cyan")
    midPoint.setOutline("cyan")
    midPoint.draw(win)
    #textual information
    Text(Point(200,50),f"Slope of the line is {m}").draw(win)
    Text(Point(200,100),f"The length of the line is {lineLength}").draw(win)

    #quiting prompt
    quit = Text(Point(200,10),"Click again to quit")
    quit.setStyle("bold")
    quit.draw(win)
    win.getMouse()
    win.close()
main()
