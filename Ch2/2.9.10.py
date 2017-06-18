# 2.9.10.py
# A program to convert Sq. Feet to Sq. Acres.

def main():
    sqft = float(input("What is the square foot area: "))
    sqacre = sqft / 43560
    print("The area is", "{0:.2f}".format(sqacre),"Acres")

main()
