# 1.10.7.py
# Chapter 1, exersice 2
# Chaos function shown on section 1.6 the magic of python
def main():
    print("This function demonstraits a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter another number between 0 and 1: "))
    n = int(input("Enter number of values to return: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{:10.6} {:10.6}".format(x, y))


main()
