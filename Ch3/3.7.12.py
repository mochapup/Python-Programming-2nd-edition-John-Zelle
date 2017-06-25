# 3.7.12.py
# This program find the sum of the cubes of natural numbers
def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact + factor**3
    print(f"The sum of the cubed natural number {n} is {fact}")

main()
