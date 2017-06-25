# 3.7.5.py
# This program calculates the cost of shipping bags of coffee
def main():
    print("This program calculates the cost of coffee including shipping and over head costs.")
    bagCost = 10.50 # per 1 pound bag
    shippingCost = 0.86 # per pound
    overhead = 1.50
    bagNum = int(input("Number of 1 pound coffee bags ordered? "))
    totalCost= (bagCost * bagNum) + (bagNum * shippingCost) + overhead
    print(f"The total cost for the order is ${totalCost}")
main()
