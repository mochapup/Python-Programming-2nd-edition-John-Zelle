# 6.8.10.py
# Program take takes in a phrase and output an acronym in uppercase letters.

def acronym(phrase):
    # create acronym List
    letters = []
    # Loops through phrase and splits into one word pieces.
    for word in phrase.split(" "):
        firstLetter = str(word[0].upper())
        letters.append(firstLetter)

    acronym = "".join(letters)
    return acronym

def main():
    print("This program takes in a phrase and outputs a acronym in upper case letters")
    phrase = input("Enter your phrase: ")
    print(f"The phrase '{phrase.title()}' is summerized to '{acronym(phrase)}'.")
main()
