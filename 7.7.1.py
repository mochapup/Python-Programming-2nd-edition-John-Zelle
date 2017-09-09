#7.7.1.py
# This program calculate sthe hourly rate and number of hours worked per week

def main():
    print("This program gives wages earned in a week period.")
    rate = float(input("What is the hourly rate? "))
    numberHours = float(input("How many hours were worked? "))

    # determines if overtime pay is included
    if numberHours > 40:
        pay = (numberHours-40) * (rate * 1.5) + 40 * rate
        print(f"The total wages are {pay} dollars")
    elif numberHours <= 40:
        pay = numberHours * rate
        print(f"The total wages are {pay} dollars")
    else:
        print("Something went wrong")

if __name__ == '__main__':
    main()
