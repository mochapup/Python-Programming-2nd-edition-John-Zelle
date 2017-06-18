# 3.7.2.py
# This program calculate the cost per square inch of a circular pizza

from math import pi

def main():
    print("""This program calculates the cost per square inch of a circular pizza
from given price and diameter""")
    price = float(input("How much is the pizza: "))
    dia = float(input("What is the pizza diameter: "))
    rad = dia/2
    sqinCost = round(price / (pi * rad ** 2),2)
    print(f"The pizza's price is ${sqinCost} per square inch")

main()
