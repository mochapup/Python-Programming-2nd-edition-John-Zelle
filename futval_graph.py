# futval_graph.py
# program calculates the future value of an investement and plots of a graph.

from graphics import *

def main():
    # Introduction
    print("The program plots the growth of a 10-year investment")

    # Get principal and interest rate
    principal = float( input("Enter the initial principal: "))
    apr = float( input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on the left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    # Draw a bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next years
        principal = principal * (1 + apr)
        # draw bar for this graph
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to exit")
    win.close()
main()
