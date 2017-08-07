# triangle2.py
import math
from graphics import *

def square(x):
    return x*x

def distance(p1, p2):
    dist = math.sprt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))
    return dist


def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on thee points")
    message.draw(win)

    # Get and draw three verticies of Triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use polygon object to draw the Triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    #calculate the perimeter of triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText(f"The perimeter is: {perim}")

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()

main()
