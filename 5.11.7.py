#5.11.7.py
#This program encodes and decodes a message using Ceaser Cipher

def encode():
    print("You are encoding a message.")
    key = int(input("Enter a key number that will encode your message: "))
    uncodedMessage = input("Enter your message: ")

    encodedMessage = []
    for ch in uncodedMessage:
        character = ord(ch) - key
        codecharacter = chr(int(character))
        encodedMessage.append(codecharacter)

    joinencodedmessage = "".join(encodedMessage)
    print(f"The encoded message is: {joinencodedmessage}")

def decode():
        print("You are decoding a message.")
        key = int(input("Enter a key number that will decode your message: "))
        encodedMessage = input("Enter your message: ")

        decodedMessage = []
        for num in encodedMessage:
            codenum = ord(num) + key
            decodecharcter = chr(int(codenum))
            decodedMessage.append(decodecharcter)

        joindecodedMessage = "".join(decodedMessage)
        print(f"The decoded message is: {joindecodedMessage}")

def main():
    print("This program Encodes and Decodes a message into random numbers.")
    choice = input("Do you want to encode a message or decode a message?: ")
    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    else:
        print("Invalid choice")

main()
