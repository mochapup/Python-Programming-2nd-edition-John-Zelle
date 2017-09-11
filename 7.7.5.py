# 7.7.5.py
# This program caluclates a person's BMI

def main():
    print("This program calculates the BMI and will tell if they are in a healthy range.")

    # requests weight and height. calculates BMI and decised health class.
    try:
        weight = float(input("What is the persons weight in LBS? "))
        height = float(input("What is the persons height in inches? "))
        bmi = (weight * 720)/(height*height)
        if bmi < 19:
            print("Your BMI is {0:0.2f}, this is below the healthy range.".format(bmi))
        elif bmi >= 19 and bmi <= 25:
            print("Your BMI is {0:0.2f}, this is in the healthy range.".format(bmi))
        elif bmi > 25:
            print("Your BMI is {0:0.2f}, this is above the helthy range.".format(bmi))
        else:
            print("Something went wrong.")
    # Costume error message
    except TypeError:
        print("\nYour inputs were not all numbers")
    except:
        print("Something went wrong.")

if __name__ == '__main__':
    main()
