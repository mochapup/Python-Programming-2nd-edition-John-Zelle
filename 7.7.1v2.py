#7.7.1.py
# This program calculate sthe hourly rate and number of hours worked per week

#defining salary functions
def overtimePay(hours,hourlyRate):
    pay = (hours-40) * (hourlyRate * 1.5) + 40 * hourlyRate
    print(f"The total wages are {pay} dollars")

def regPay(hours,hourlyRate):
    pay = hours * hourlyRate
    print(f"The total wages are {pay} dollars")
# defining main function
def main():
    print("This program gives wages earned in a week period.")
    rate = float(input("What is the hourly rate? "))
    numberHours = float(input("How many hours were worked? "))

    # determines if overtime pay is included
    if numberHours > 40:
        overtimePay(numberHours,rate)
    elif numberHours <= 40:
        regPay(numberHours,rate)
    else:
        print("Something went wrong")

if __name__ == '__main__':
    main()
