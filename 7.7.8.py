# 7.7.8.py
# This program takes in the age and number of years of being a citizen
# outputs elibility to become US Rep. or US Senator.

def main():
    print("This program will evaluate a person's eligibility to become an US Senator or Representative.")
    print("Are you atleast 25 years old and have been an US citizen for 7 years?")
    checkpoint = str(input("Enter yes or no.\n>"))
    if checkpoint == "yes":
        try:
            age = int(input("What is the person's age?\n>"))
            citizenship = int(input("How many years has the person been an US citizen?\n>"))
            status_check(age, citizenship)
        except:
            print("Something went wrong, Please enter whole numbers.")
    elif checkpoint == "no":
        print("The person is not eligible yet to be an US Senator or Representative.")
    else:
        print("Something when wrong")

# Checks eligibility for US senator vs rep.
def status_check(age,citizenship):
    try:
        if age >= 30 and citizenship >= 9:
            print("Congratulations! The person is eligible to become an US Senator and Representative.")
        elif age>= 25 and citizenship >= 7:
            print("Congratulations! The person is eligible to become an US Representative.")
        else:
            print("This person is not eligible to become an US Senator or Representative.")
# Exception raised if whole numbers are not entered
    except:
        print("Something went wrong. Please enter whole numbers.")

# Calling program
if __name__ == '__main__':
    main()
