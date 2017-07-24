# userfile.py
# Program to create a file of user names in batch mode.
def main():
    print("This program creates a file of user names from a file of names")

    # Get the file name
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the user names go in? ")

    # Open the files
    infile = open(infileName,"r")
    outfile = open(outfileName,"w")

    # process each line of the input file
    for line in infile:
        # get the first and last namee from file
        first, last = line.split()
        # create username
        uname = (first[0]+last[:7]).lower()
        # write it to the outfile
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()
