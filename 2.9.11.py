# 2.9.11.py
# A program  to convert Sq. Feet to Sq. Acres.
print("This program will calculate math problems")

def main():
    run = 1
    while run ==1:
        problem = input("Enter a calculation: ")
        solution = eval(problem)
        print(problem, "=", solution)
        end = input("Enter 'y' to exit or 'n' to continue")
        if end == 'y':
            run = 0

main()
