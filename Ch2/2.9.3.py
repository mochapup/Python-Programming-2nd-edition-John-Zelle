# 2.9.3.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This is a program to convert Celsius temps to Fahrenheit ")
    celsius = float(input("What are 5 the Celsius tempratures? "))
    for i in range(5):
        fahrenheit = 9/5 * celsius + 32
        print("The temprature is ", fahrenheit, "degrees Fahrenheit")

main()
