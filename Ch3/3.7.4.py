# 3.7.4.py
# This program determines the distance of a lightening bolt.
def main():
    print("""This program determines the distance of a lightening bolt strike
based on the time elapsed between flash and sound of thunder.""")
    speedOfSoundFtSec = 1100 # Speed of sound approximate 1100 feet/sec.
    mile = 5280 # distance of a mile in feet.
    t = float(input("How many seconds passed after the flash when you heard thunder? "))
    dist = (speedOfSoundFtSec * t) / mile
    print(f"The distance of the lightening strike is {dist} miles.")
main()
