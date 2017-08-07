# 5.11.14.py
# This is a word counting program. The program reads the file, counts the lines, words and letter in the file.
#
def main():
    print("This program counts the lines, words, and letters in a file")

    # Get the file name
    infileName = input("What file do you to count:  ")

    linecount = 0
    wordcount = 0
    lettercount = 0
    #
    with open(infileName, 'r') as infile:
    # process each line of the input file
        for line in infile:
            linecount += 1
            wordcount += len(line.split())
            lettercount += len(line)
            # write it to the outfile
    print(f"Lines in the file: {linecount}\nWords in the file: {wordcount}\nLetters in the file: {lettercount}")

    # close both files
    infile.close()


main()
