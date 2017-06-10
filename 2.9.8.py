# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    fahrenheit = int(input("What is the Fahrenheit temprature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temprature is", "{0:.2f}".format(celsius),"degrees Celsius")

main()
