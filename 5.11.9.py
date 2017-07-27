#5.11.9.py
# this program counts the number of words ina  sentence

def main():
    print("This program counts the number of words in a sentence")
    sentence = input("Enter your sentence: ")
    count = len(sentence.split())
    print(f"There are {count} words.")

main()
