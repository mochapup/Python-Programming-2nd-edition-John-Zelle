#5.11.10.py
# this program calculates the average word length in a sentence

def main():
    print("This program calculates the average word length in a sentence")
    sentence = input("Enter your sentence: ")
    count = len(sentence.split())
    words = sentence.split()
    sumWords = 0
    for word in words:
        wordLength = len(word)
        sumWords += wordLength
    average = sumWords/count
    print(f"the average length of words is {average} letters.")

main()
