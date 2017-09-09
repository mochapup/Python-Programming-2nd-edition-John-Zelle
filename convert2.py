# convert2.py
# A program to convert Celsius temps to Fahrenheit
# This version issues heat and cold warnings.

def main():
    celsius = float(input("What is the Celsius temprature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temprature is ", fahrenheit, "degrees Fahrenheit")

    # Prints warnings for extreme tempratures
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrr. Be sure to dress warmly!")
main()
