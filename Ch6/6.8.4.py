# 6.8.4.py
# Program to calculates the sum of natural numbers and sum of cubed natural numbers


def sumN(n):
    return sum(range(1,n+1))

def sumNCubes(n):
    return sum(i**3 for i in range(1, n+1))  # sum of cubed natural numbers

def main():
    print("This program calculates the sum of natural numbers and sum of cubed natural numbers")
    num = int(input("How many natural numbers to sum: "))
    s = sumN(num)
    c = sumNCubes(num)
    print(f"The sum of all natural numbers to {num} is {s}.\nThe sum of all cubed natural numbers to {num} is {c}.")

main()
