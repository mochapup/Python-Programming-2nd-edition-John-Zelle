# addinterest2.py

def addInterest(balance, rate):
    for i in range(len(balance)):
        balance[i] = balance[i] * (rate + 1)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    amount = addInterest(amounts, rate)
    print(amounts)
test()
