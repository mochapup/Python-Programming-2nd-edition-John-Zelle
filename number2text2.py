# number2text2.py
# A program to convert a sequence of Unicode numbers into a string of textual

def main():
    print("This program converts a sequence of Unicode numbers into the string of text it reperesents.\n")

    # Get message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    #Loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codenum = int(numStr)    # Convert digits to a number
        chars.append(chr(codenum))    # accumulate new character

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()
