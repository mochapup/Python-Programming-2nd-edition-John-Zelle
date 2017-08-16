# 6.8.11.py
# Fuction squares each number in a list of numbers

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    numlist = [2,3,5,5]
    squareEach(numlist)
    print(numlist)

main()
