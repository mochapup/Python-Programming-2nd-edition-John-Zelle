# quadratic6.py
# a program that computes real roots of a quadratic equation

import math # Makes the math library aviliable

def main():
    print("This program finds the real solutions to a quadratic\n")
    # requests coefficient

    # using try function with except function to catch errors with custome message.
    try:
        a, b, c = eval(input("Please enter 'a, b, c' coefficient: "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots.")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")

main()
