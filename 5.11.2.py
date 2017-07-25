# 5.11.2.py
# Ptogram take a 5 point score and converts it into a grade

def main():
    print("This program takes a 5 point score and converts it into a Letter Grade.")
    score = input("What is your score: ")
    # List of Letter grades corresponding with Letter grades
    grades = ["F","F","D","C","B","A"]
    letScore = grades[int(score)]

    # output the letter grade
    print(f"The score {score} is a grade {letScore}.")

main()
