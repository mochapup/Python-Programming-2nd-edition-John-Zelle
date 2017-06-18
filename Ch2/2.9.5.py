# 2.9.5.py
# A program to compute the value of an investment
# carried given years into the future

def main():
    print("This program calculates the future value")
    years = int(input("How many years in the future: "))
    print(f"of a {years} year investment")
    principal = float( input("Enter the initial principal: "))
    apr = float( input("Enter the annual interest rate: "))
    for i in range(years):
         principal = float(principal * (1 + apr))
    print(f"The value in {years} years is:", "${0:.2f}".format(principal))

main()
