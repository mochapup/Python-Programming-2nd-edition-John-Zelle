# change2.py
# A program to calculate the value of some change into dollars
# This version reperesents the total cash in cents

def main():
    print ("Change Counter\n")

    print("Please neter the count of each coin type.")
    quaters = int(input("Quareters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    total = quaters * 25 + dimes * 10 + nickles * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

main()
