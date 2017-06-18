# 1.10.6B.py
# Chapter 1, exersice 2
# Chaos function shown on section 1.6 the magic of python
def main():
    print("This function demonstraits a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    n = int(input("Enter number of values to return: "))
    for i in range(n):
        x = 3.9 * (x - x * x)
        print(x)

main()
