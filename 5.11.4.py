# 5.11.4.py
# Ptogram take takes in a phrase and output an acronym in uppercase letters.

def main():
    print("This program takes in a phrase and outputs a acronym in upper case letters")
    phrase = input("Enter your phrase: ")
    # creat acronym List
    letters = []
    # Loops through phrase and splits into one word pieces.
    for word in phrase.split(" "):
        firstLetter = str(word[0].upper())
        letters.append(firstLetter)

    acronym = "".join(letters)
    print(f"The phrase '{phrase.title()}' is summerized to '{acronym}'.")
main()
