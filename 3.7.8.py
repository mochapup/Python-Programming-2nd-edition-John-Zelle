# 3.7.8.py
# This program figures out the date of easter
def main():
    print("""This program figures out the Gregorianc Epact,
or the number of days since the previous new moon from January 1st for a given year""")
    year = int(input("Enter a year: "))
    C = year // 100
    epact = (8+(C//4)-C+((8*C+13)//25)+11*(year%19))%30
    print(f"There are {epact} days between January 1st and the previous new moon for {year}")

main()
