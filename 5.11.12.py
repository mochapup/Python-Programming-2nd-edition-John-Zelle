# futval.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    principal = float( input("Enter the initial principal: "))
    apr = float( input("Enter the annual interest rate: "))
    years = int(input("How many years in the future: "))
    print("of a 10 year investment")
    # Title of table
    title = "Year   Value"
    # outputs table title and table dashes
    print("\n {}\n{}".format(title,"-"*int(14)))
    print("  {:00.0f} {:10.2f}".format(0, principal)) # Outputs initial principal on table
    # iterates through years
    for i in range(1,years+1):
         principal = float(principal * (1 + apr))
         print("  {:00.0f} {:10.2f}".format(i, principal))
main()
