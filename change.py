# change.py
# A program ro calculate the value of some change in dollars

def main():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    print("\nThe total value of your change is $",total)

main()
