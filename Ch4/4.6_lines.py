# 4.6_lines.py(Tic-Tac-Toe)
from graphics import *

# Create a default 200x200 window
win = GraphWin("Tic-Tac-Toe")

# Set coordinates to go from (0,0) in the lower left
# to (3,3) to the upper right
win.GraphWin(0.0,0.0,3.0,3.0)

# draw vertical lines
Line(Point(1,0), Point(1,3)).draw(win)
Line(Point(2,0), Point(2,3)).draw(win)

# Draw horizontal lines
Line(Point(0,1), Point(3,1)).draw(win)
Line(Point(0,2), Point(3,2)).draw(win)

input("Press <Enter> to quit")
win.close()
