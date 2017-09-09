# 7.7.3.py
# This program accepts a quiz score and calculates a correspodning grade

def main():
    print("This program takes a 100-point grade and converts it into a letter grade")

    # converts number grade to letter grade
    try:
        numGrade = int(input("What is the number grade? "))
        if numGrade < 60 and numGrade > -1:
            print("Your letter grade is F")
        elif numGrade >=60 and numGrade < 70:
            print("Your letter grade is D")
        elif numGrade >=70 and numGrade < 80:
            print("Your letter grade is C")
        elif numGrade >=80 and numGrade < 90:
            print("Your letter grade is B")
        elif numGrade >=90 and numGrade <= 100:
            print("Your letter grade is A")
        else:
            print("That number is out of range")
    # custome error message
    except:
        print("Something went wrong")

# Calling program
if __name__ == '__main__':
    main()
