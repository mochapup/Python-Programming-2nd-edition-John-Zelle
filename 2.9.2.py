# 2.9.2.py
# A simple program to average two exam scores
# Illustraits the use of multiple inputs

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = input("Enter three scores seperated by a comma: ").split(",")
    average = (float(score1) + float(score2) + float(score3)) / 3

    print("The average of the scores is:", average)
main()
