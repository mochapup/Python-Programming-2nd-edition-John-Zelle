# dateconverter.py
# Convert a date in the form "mm/dd/yyyy" to "month day, year"

def main():
    # get the date
    dateStr = input("Please enter the date in (mm/dd/yyyy) format: ")

    #split the components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # Convert the monthStr to month name.
    months = ["January", "Febuarary", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]

    # Output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)
main()
