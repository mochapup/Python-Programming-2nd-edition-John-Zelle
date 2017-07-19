# text2numbers.py

# A program to convert a textual message into a sequence of numbers, utilizing the underlaying Unicode Encoding
def main():
    print("This program converts a textual message into a sequence of numbers repersenting the Unicode encoding of the message.\n")

    # Get the message to encode
    message = input("Please enter your message to encode: ")\

    print("\nHere are the unicodes: ")

    # Loop through the message and print out Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print() # break line before prompt

main()
