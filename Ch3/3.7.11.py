# 3.7.11.py
# This program finds the sum of natural numbers

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact + factor
    print(f"The sum of natural number {n} is {fact}")

main()
