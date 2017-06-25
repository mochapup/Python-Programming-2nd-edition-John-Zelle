# 3.7.6.py
# This program calculate the slope between two points of a plane
def main():
    print("This program calculates the slope of a line between two points")
    x1 = float(input("What is the first point's X coordinate: "))
    y1 = float(input("What is the first point's y coordinate: "))
    x2 = float(input("What is the second point's X coordinate: "))
    y2 = float(input("What is the second point's y coordinate: "))
    slope = (y2 - y1)/(x2 - x1)
    fractionSlopeY = int(y2 - y1)
    fractionSlopeX = int(x2 - x1)
    print(f"The slope between the two points is {slope} or {fractionSlopeY}/{fractionSlopeX}")
main()
