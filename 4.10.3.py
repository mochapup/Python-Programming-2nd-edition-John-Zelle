# 4.10.3.py
from graphics import *

def main():
    win = GraphWin("",400, 400)
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    leftEye = Circle(Point(1,3), .5)
    leftEye.setFill("white")
    leftEye.draw(win)
    rightEye = Circle(Point(3,3), .5)
    rightEye.setFill("white")
    rightEye.draw(win)
    leftPupil = Circle(Point(1,3), .25)
    leftPupil.setFill("blue")
    leftPupil.draw(win)
    rightPupil = Circle(Point(3,3), .25)
    rightPupil.setFill("blue")
    rightPupil.draw(win)
    nose = Circle(Point(2,2), .5)
    nose.draw(win)
    mouth = Line(Point(3,1), Point(1,1))
    mouth.setFill("black")
    mouth.draw(win)

    win.getMouse()
    win.close()
main()
