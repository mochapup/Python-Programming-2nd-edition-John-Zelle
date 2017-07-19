# number2text.py
# A program to convert a sequence of Unicode numbers into a string of textual

def main():
    print("This program converts a sequence of Unicode numbers into the string of text it reperesents.\n")

    # Get message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    #Loop through each substring and build Unicode message
    message = " "
    for numStr in inString.split():
        codenum = int(numStr)    # Convert digits to a number
        message = message + chr(codenum)    # concatenate character to message

    print("\nThe decoded message is:", message)

main()
