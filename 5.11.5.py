# 5.11.5.py
# converts a single sequence of letters into the alphabetical placement

def main():
    print("This program calculates the sum of the numeric value of your name.")
    name = input("Enter your name: ")
    name = name.lower()
    numericValue = []
    for character in name:
        number = ord(character)-96
        numericValue.append(number)
    numericSum = sum(numericValue)
    print(f"The numeric value of your name is {numericValue}={numericSum}.")
main()
