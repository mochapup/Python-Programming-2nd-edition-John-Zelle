# 3.7.3.py
# This program determines the moleculer weight of a hydrocarbon
# Atom weight given h=1.0079, c=12.011, o=15.9994

def main():
    print("""This program determines the molecular weight of a hydrocarbon based\n
on the number of hydrongen, carbon, and oxygen atoms.""")
    h = 1.0079
    c = 12.011
    o = 15.9994
    hnum = float(input("How many hydrogen atoms are there: "))
    cnum = float(input("How many carbon atoms are there: "))
    onum = float(input("How many oxygen atoms are there: "))

    weight = (hnum*h) + (cnum*c) + (onum*o)
    print(f"The weight of molecular weight of the hydrocarbon is {weight} grams")
main()
