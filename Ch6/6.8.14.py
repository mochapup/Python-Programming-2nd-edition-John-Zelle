# 6.8.14.py
# this program will print the sum of squared numbers read from a file.

def toNumbers(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def sumList(nums):
    return sum(nums)

def main():
    # Get the file name
    infileName = input("What file are the names in? ")
    infile = open(infileName,"r")
    for line in infile:
        numList = line.split()
        toNumbers(numList)
        squareEach(numList)
        print(sumList(numList))

main()
