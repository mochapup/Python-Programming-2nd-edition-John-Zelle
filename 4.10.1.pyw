# 4.10.1.pyw

from graphics import *

def main():
    win = GraphWin("",400, 400)
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    shape = Rectangle(Point(1.5,1.5), Point(2.5,2.5))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        shape2 = shape.clone()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2.move(dx,dy)
        shape2.draw(win)

    quit = Text(Point(2,3.5),"Click again to quit")
    quit.setStyle("bold")
    quit.draw(win)
    win.getMouse()
    win.close()

main()
