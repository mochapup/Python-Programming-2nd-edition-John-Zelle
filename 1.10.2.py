# 1.10.2.py
# Chapter 1, exersice 2
# Chaos function shown on section 1.6 the magic of python
def main():
    print("This function demonstraits a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
