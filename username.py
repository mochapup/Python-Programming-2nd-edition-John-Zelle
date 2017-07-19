# username.py
# simple string processing program to generate usernames.

def main():
    print("This program generates computer user names.\n")

    # get the users first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate the first initial with 7 chars of your last name
    uname = first[0] + last[:7]

    # output the user name
    print("Your user name is: ",uname)

main()
