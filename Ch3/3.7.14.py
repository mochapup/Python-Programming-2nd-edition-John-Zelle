# 3.7.14.py
# This program finds the average of a defined quantity of numbers entered by the user


def main():
    print("This program finds the average of a series of given numbers")
    n = int(input("How many numbers will be entered? "))
    a = 0
    b = 0
    while b < n:
        b += 1
        a += float(input("Enter your number: "))
        avg = a/n
    print(f"The average of the {n} numbers is {avg}.")
main()
