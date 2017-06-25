# 3.7.9.py
# This program calculates the area of a triangle given the length of three sides
from math import sqrt
def main():
    print("This program calculates the area of a triangle given the length of of three sides.")
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"The triangle's area is {area}")

main()
