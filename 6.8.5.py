# 6.8.5.py
# This program calculate the cost per square inch of a circular pizza

from math import pi

def pieArea(r):
    return round((pi * r ** 2),2) # returns area of pie in sqin

def sqinCost(price,r):
    return round(price / (pi * r ** 2),2) # returns  price per sqin

def main():
    print("""This program calculates the cost per square inch of a circular pizza
from given price and diameter""")
    price = float(input("How much is the pizza: "))
    dia = float(input("What is the pizza diameter: "))
    rad = dia/2
    print(f"The pizza's area is {pieArea(rad)} square inches and the price is ${sqinCost(price,rad)} per square inch")

main()
