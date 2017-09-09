# 6.8.7.py
# this program computes the nth fibonacci sequence given by user

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return  fib(n-1)+fib(n-2)
        
def main():
    print("This program calculates the nth Fibonacci sequence number")
    n = int(input("Enter the fibonacci number you want to be calulated: "))

    print(f"The Fibonacci number of {n} is {fib(n)}")
main()
