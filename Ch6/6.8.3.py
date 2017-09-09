# 6.8.3.py
# Program to calculate the volume and surface area of a sphere

from math import pi

def sphereArea(radius):
    area = 4*pi*radius**2 # Area formula
    return area

def sphereVolume(radius):
    volume = (4/3*pi*radius**3) # Volume formula
    return volume

def main():
    print("The program calculates the volume and surface area of a sphere")
    rad = float(input("What is the radius of the sphere: "))
    vol = sphereVolume(rad)
    area = sphereArea(rad)
    print(f"The volume of the sphere is {vol}\nThe area of the sphere is {area}")

main()
