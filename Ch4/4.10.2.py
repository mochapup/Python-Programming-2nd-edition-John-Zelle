# 4.10.2.pyw

from graphics import *

def main():
    win = GraphWin("",400, 400)
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    shape1 = Circle(Point(2,2), 2)
    shape1.setFill("white")
    shape1.draw(win)
    shape2 = Circle(Point(2,2), 1.6)
    shape2.setFill("black")
    shape2.draw(win)
    shape3 = Circle(Point(2,2), 1.2)
    shape3.setFill("blue")
    shape3.setOutline("blue")
    shape3.draw(win)
    shape4 = Circle(Point(2,2), 0.8)
    shape4.setFill("red")
    shape4.setOutline("red")
    shape4.draw(win)
    shape5 = Circle(Point(2,2), 0.4)
    shape5.setFill("yellow")
    shape5.setOutline("yellow")
    shape5.draw(win)

    win.getMouse()
    win.close()
main()    
