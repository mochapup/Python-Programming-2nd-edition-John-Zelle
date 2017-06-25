# 3.7.7.py
# This program determines the distance between two points
from math import sqrt
def main():
    print("This program calculates the distance between two points")
    x1 = float(input("What is the first point's X coordinate: "))
    y1 = float(input("What is the first point's y coordinate: "))
    x2 = float(input("What is the second point's X coordinate: "))
    y2 = float(input("What is the second point's y coordinate: "))
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"The distance between the two points is {dist}S")
main()
