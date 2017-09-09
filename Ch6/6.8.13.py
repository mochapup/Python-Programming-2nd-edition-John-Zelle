# 6.8.13.py
# Fuction converts each string into a number in a list of strings

def toNumbers(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])

def main():
    numlist = ["2","3","5","5"]
    toNumbers(numlist)
    print(numlist)

main()
