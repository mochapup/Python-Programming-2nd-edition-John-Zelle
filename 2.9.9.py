# 2.9.9.py.py
# A program to convert Kilometers to Miles.

def main():
    km = float(input("What is the distance in Kilometers: "))
    mi = km / 2 + (km / 8)
    print("The distance is", "{0:.2f}".format(mi),"Miles")

main()
