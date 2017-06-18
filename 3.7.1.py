# 3.7.1.py
# Program to calculate the volume and surface area of a sphere

from math import pi


def main():
    print("The program calculates the volume and surface area of a sphere")
    rad = float(input("What is the radius of the sphere: "))
    vol = (4/3*pi*rad**3) # Volume formula
    area = 4*pi*rad**2 # Area formula
    print(f"The volume of the sphere is {vol}\nThe area of the sphere is {area}")

main()
