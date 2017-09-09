# quadratic2.py
#   a program that computes real roots of a quadratic equation
#   Illustraits the use of the math library
#   Note: this program crashes if the equation has no real roots

import math # Makes the math library aviliable

def main():
    print("This program finds the real solutions to a quadratic\n")
    # requests coefficient
    a, b, c = eval(input("Please enter 'a, b, c' coefficient: "))
    discrim = b * b - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are: ", root1, root2)

main()
