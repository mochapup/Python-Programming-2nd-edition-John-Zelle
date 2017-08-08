# futval_graph3.py
# program calculates the future value of an investement and plots of a graph.

from graphics import *

def createLabeledWindow():
    # Create a graphics window with labels on the left edge
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5K').draw(window)
    Text(Point(-1, 5000), ' 5.0K').draw(window)
    Text(Point(-1, 7500), ' 7.5K').draw(window)
    Text(Point(-1, 10000), ' 10.0K').draw(window)
    return window

def drawBar(window, year, height):
    #Draw a bar in a window for given year with given height
    bar = Rectangle(Point(year,0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    # Introduction
    print("The program plots the growth of a 10-year investment")
    # Get principal and interest rate
    principal = float( input("Enter the initial principal: "))
    apr = float( input("Enter the annualized interest rate: "))
    win = createLabeledWindow()
    # Draw a bar for initial principal
    drawBar(win, 0, principal)
    # Draw bars for successive years
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to exit")
    win.close()
main()
