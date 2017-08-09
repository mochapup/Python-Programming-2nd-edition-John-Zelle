# 6.8.9.py
# Ptogram take a 100 point score and converts it into a grade

def grade(score):
    if score >= 90 and score <= 100:
        print("You recieved an A")
    elif score >= 80 and score < 90:
        print("You recieved a B")
    elif score >= 70 and score < 80:
        print("You recieved a C")
    elif score >= 60 and score < 70:
        print("You recieved a D")
    else :
        print("You recieved a F")

def main():
    print("This program takes a 100 point score and converts it into a Letter Grade.")
    score = int(input("What is your score: "))
    # List of Letter grades corresponding with Letter grades
    grade(score)
main()
