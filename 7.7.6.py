# 7.7.6.py
# This program calculates speeding ticket penalties

# defining the penalty
def penalty():
    penaltyCost = (speedTraveled - speedLimit) * 5 + 50
    # chciking if additional 200 dollar fine is required
    if speedTraveled >= 90:
        penaltyCost = penaltyCost + 200
    else:
        penaltyCost = penaltyCost

    print(f"The speed traveled was {speedTraveled} MPH and the speed limit was {speedLimit} MPH")
    print(f"This speed is illeagle and a penalty of {penaltyCost} Dollars will be applied")

print:("This program calculates the penalty cost of a speeding ticket")
#requesting speed limit
speedLimit = int(input("What is the speed limit? "))

#requests speed traveled
speedTraveled = int(input("What is the speed traveled? "))
#Checking if spped was legal
if speedTraveled > speedLimit:
    penalty()
else:
    print("Speed limit was not exceeded. No penalty")
