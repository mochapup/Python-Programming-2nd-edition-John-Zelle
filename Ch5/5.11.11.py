# 5.11.11.py
# Chapter 5, exersice 11
# Chaos function shown on section 1.6 the magic of python improved
# to contain a better table
def main():
    print("This function demonstraits a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter another number between 0 and 1: "))
    n = int(input("Enter number of values to return: "))
    table = ["\nindex", x, y, "-"*30]

    print(f"{table[0]}     {table[1]}         {table[2]}\n{table[3]}")

# for loop to iterate numbers
    for i in range(1,n+1):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("  {:00.0f}   {:10.6f}   {:10.6f}".format(i, x, y))

main()
