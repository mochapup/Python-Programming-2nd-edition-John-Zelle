#7.7.2.py
# This program accepts a quiz score and calculates a correspodning grade

def main():
    print("This program takes a grade 0 - 5 and converts it into a letter grade")

    # converts number grade to letter grade
    try:
        numGrade = int(input("What is the number grade? "))
        if numGrade < 2:
            print("Your letter grade is F")
        elif numGrade == 2:
            print("Your letter grade is D")
        elif numGrade == 3:
            print("Your letter grade is C")
        elif numGrade == 4:
            print("Your letter grade is B")
        elif numGrade == 5:
            print("Your letter grade is A")
        else:
            print("That number is out of range")
    # custome error message
    except:
        print("Something went wrong")

# Calling program
if __name__ == '__main__':
    main()
