# 7.7.7.py
# This program calculates the amount of pay for a baby sitter, based on hours worked.
# Program takes in consideration of payscale before and after children are in bed.

def main():
    print("This program calculates the amount of pay earned by a babysitter.")
    start = input("What did the babysitter start?")
    end = input("What time did babysitter finish?")
    try:
        if get_min(end) <= get_min('9:00') and get_min(start) <= get_min('9:00'):
            worktime = (get_min(end) - get_min(start)) / 60
            pay = worktime * 2.50
            print(f"The babysitter worked {worktime:00.2f} hours and will be payed {pay:00.2f} dollars.")

        elif get_min(start) >= get_min('9:00'):
            worktime = (get_min(end) - get_min(start)) / 60
            pay = worktime * 1.75
            print(f"The babysitter worked {worktime:00.2f} hours and will be payed {pay:00.2f} dollars.")

        else:
            beforebed_worktime = get_min('9:00') - get_min(start)
            afterbed_worktime = get_min(end) - get_min('9:00')
            worktime = (get_min(end) - get_min(start)) / 60
            pay = ((beforebed_worktime / 60) * 2.50) + ((afterbed_worktime / 60) * 1.75)
            print(f"The babysitter worked {worktime:00.2f} hours and will be payed {pay:00.2f} dollars.")
    except:
        print("Something went wrong, please enter times in 'hh:mm' format")

# Breaks down the hh:mm format to int number of minutes.
def get_min(time_str):
    h, m = time_str.split(':')
    return int(h) * 60 + int(m)

# Calling program
if __name__ == '__main__':
    main()
