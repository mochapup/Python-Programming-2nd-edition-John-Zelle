# 2.9.7.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value of a fixed amount each year\nof a given year investment")

    years = int(input("How many years in the future: "))
    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the anual interest rate: "))
    periods = int(input("Enter the number of times that the interest id compounded each year: "))
    eachYear = float(input("How much do you invest each year: "))
    for i in range(years * periods):
         principal = principal * (1 + (rate/periods)) + eachYear
    print(f"The value in {years} years is:", "${0:.2f}" .format(principal))

main()
