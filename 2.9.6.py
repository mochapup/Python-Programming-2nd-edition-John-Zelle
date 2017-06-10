# 2.9.6.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value of a fixed amount each year")

    years = int(input("How many years in the future: "))
    print(f"of a {years} year investment")
    principal = float( input("Enter the initial principal: "))
    apr = float( input("Enter the annual interest rate: "))
    eachYear = float(input("How much do you invest each year: "))
    for i in range(years):
         principal = principal * (1 + apr) + eachYear
    print(f"The value in {years} years is:", "${0:.2f}" .format(principal))

main()
