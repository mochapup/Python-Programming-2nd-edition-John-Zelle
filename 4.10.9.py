# 4.10.9.py
# This program displays information about a rectangle drawn by the user.

# import libraries
from graphics import *

def main():
    win = GraphWin("Rectangle Information",400, 400)
    for i in range(1):
        p1 = win.getMouse()
        p2 = win.getMouse()

    # rectangle shape
    rect = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY())).draw(win)
    # variables needed
    rectLen = p2.getY()-p1.getY()
    rectWidth = p2.getX()-p1.getX()
    area = rectWidth*rectLen
    perimeter = (rectLen*2) + (rectWidth*2)
    # textual information
    Text(Point(200,50),f"Area of the Rectangle is {area}").draw(win)
    Text(Point(200,100),f"Perimeter of the Rectangle is {perimeter}").draw(win)

    #quiting prompt
    quit = Text(Point(200,10),"Click again to quit")
    quit.setStyle("bold")
    quit.draw(win)
    win.getMouse()
    win.close()
main()
