# 5.11.1.py
# Convert day month and year numbers into two date formats

def main():
    # get the day month and year
    day, month, year = int(input("Enter day, month, and year numbers: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    # Months
    months = ["January", "Febuarary", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]

    monthStr = months[int(month)-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)

    # Output result in month day, year format
    print("The converted date is {date1} or {date2}.")
main()
