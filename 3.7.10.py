# 3.7.10.py
# This program determines the length of a ladder required given the height of house and angle of ladder.
import math

def main():
    print("This program determines the length of a ladder required given height of house and angle of ladder")
    height = float(input("Enter the height of the house: "))
    angle = float(input("Enter the desired angle: "))
    rad = (math.pi/180)*angle
    length = height / math.sin(rad)
    print(f"The required ladder length is {length}")

main()
