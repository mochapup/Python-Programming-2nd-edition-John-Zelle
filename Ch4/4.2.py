# 4,2,py
# Graphics window with two dots
from graphics import *

win = GraphWin()
p = Point(50, 60)
p.draw(win)
p2 = Point(140, 100)
p2.draw(win)

input("press <Enter> to quit")
win.close
