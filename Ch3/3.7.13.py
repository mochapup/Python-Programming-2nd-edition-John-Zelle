# 3.7.13.py
# This program sums a defined quantity of numbers entered by the user


def main():
    print("This progrm sums a series of given numbers")
    n = int(input("How many numbers will be entered? "))
    a = 0
    b = 0
    while b < n:
        b += 1
        a += float(input("Enter your number: "))
    print(f"The sum of the {n} numbers is {a}.")
main()
