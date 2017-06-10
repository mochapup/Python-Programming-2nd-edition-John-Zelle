# 2.9.3.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This is a program prints a table of celsius and fahrenheit tempratures ")
    print("Celsius","Fahrenheit")
    celsius =0
    for i in range(11):
        fahrenheit = float(9/5 * celsius + 32.1)
        print("{:2} {:10}".format(celsius, fahrenheit))
        celsius = celsius + 10
main()
