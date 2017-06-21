# 3.7.16.py
# this program computes the nth fibonacci sequence given by user

def main():
    print("This program calculates the nth Fibonacci sequence number")
    n = int(input("Enter the fibonacci number you want to be calulated: "))
    a,b = 1,1
    num = n-2
    for i in range(num):
        a,b = b,a+b
    print(f"The Fibonacci number of {n} is {b}")
main()
