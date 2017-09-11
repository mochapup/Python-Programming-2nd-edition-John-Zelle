# 7.7.4.py
# This program calculates the class standing from number of credits earned

def main():
    print("This program takes number of credits earned by a student and returns their standing")

    # converts number grade to letter grade
    try:
        credits = int(input("How many credits were earned? "))
        if credits < 7 and credits >= 0:
            print("The student is a Freshman")
        elif credits >= 7 and credits < 16:
            print("The student is a Sophomore")
        elif credits >= 16 and credits < 26:
            print("The student is a Junior")
        elif credits >= 26:
            print("The student is a Senior")
        else:
            print("That number is out of range")
    # custome error message
    except TypeError:
        print("\nYour inputs were not all numbers")
    except:
        print("Something went wrong")

# Calling program
if __name__ == '__main__':
    main()
