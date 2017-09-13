#7.7.2.py
# This program accepts a quiz score and calculates a correspodning grade

#Grade list
grades=["F","F","D","C","B","A"]
# defining grade functions
def printGrade(num):
    print("Your letter grade is a",grades[num])
#defining main function
def main():
    print("This program takes a grade 0 - 5 and converts it into a letter grade")

    # converts number grade to letter grade
    try:
        numGrade = int(input("What is the number grade? "))
        if numGrade < 6 and numGrade >= 0:
            printGrade(numGrade)
        else:
            print("That number is out of range")
    # custome error message
    except:
        print("Something went wrong")

# Calling program
if __name__ == '__main__':
    main()
