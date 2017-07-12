# 4.10.10.py
# This program displays information about a rectangle drawn by the user.

# import libraries
from graphics import *
from math import sqrt

def main():
    win = GraphWin("Triangle Information",400, 400)
    for i in range(1):
        p1 = win.getMouse()
        p2 = win.getMouse()
        p3 = win.getMouse()

    # components needed
    aX = p1.getX()-p2.getX()
    aY = p1.getY()-p2.getY()
    bX = p2.getX()-p3.getX()
    bY = p2.getY()-p3.getY()
    cX = p3.getX()-p1.getX()
    cY = p3.getY()-p1.getY()
    a = sqrt((aX**2)+(aY**2))
    b = sqrt((bX**2)+(bY**2))
    c = sqrt((cX**2)+(cY**2))
    s = ((a + b + c)/2)
    # Calculating area
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    # triangle shape
    triangle = Polygon(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()), Point(p3.getX(),p3.getY())).draw(win)

    # textual information
    Text(Point(200,50),f"Area of the Triangle is {area}").draw(win)

    #quiting prompt
    quit = Text(Point(200,10),"Click again to quit")
    quit.setStyle("bold")
    quit.draw(win)
    win.getMouse()
    win.close()
main()
