# A simple program to average two exam scores
# Illustraits the use of multiple inputs

def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores seperated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)
main()
