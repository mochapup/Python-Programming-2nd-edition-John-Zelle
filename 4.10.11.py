# 4.10.11.py
# import libraries
from graphics import *
from math import sqrt

def main():
    win = GraphWin("Triangle Information",400, 400)
    for i in range(1):
        p1 = win.getMouse()
        p2 = win.getMouse()
        p3 = win.getMouse()
        p4 = win.getMouse()
        p5 = win.getMouse()
    houseWidth = p2.getX()-p1.getX()
    doorWidth = houseWidth/10
    windowWidth = doorWidth/2
    house = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY())).draw(win)
    door = Rectangle(Point((p3.getX()+doorWidth),p3.getY(), Point((p3.getX()+doorWidth),p1.getY()))).draw(win)
    window = Rectangle(Point((p4.getX()+windowWidth),(p4.getY()+windowWidth), Point((p4.getX()-windowWidth),(p4.getY()-windowWidth)))).draw(win)
    roof = Polygon(Point(p1.getX(),p2.getY()), Point(p2.getX(),p2.getY()), Point(p5.getX(),p5.getY())).draw(win)

    quit = Text(Point(200,10),"Click again to quit")
    quit.setStyle("bold")
    quit.draw(win)
    win.getMouse()
    win.close()
main()
