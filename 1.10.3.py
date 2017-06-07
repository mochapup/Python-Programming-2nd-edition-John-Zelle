# 1.10.3.py
# Chapter 1, exersice 2
# Chaos function shown on section 1.6 the magic of python
def main():
    print("This function demonstraits a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()


#  In the original chaos function, the out were very chaotic, unpredictable. This was due to the input creating a product with 3.9.
# Now that we changed 3.9 to2.0, the product is less chaotic, even linear, and products eventually equal a constant 0.5.
