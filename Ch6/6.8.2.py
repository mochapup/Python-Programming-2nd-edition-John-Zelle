# 6.8.2.py
# This program prints this first ten verses of "The Ants Go Marching"

def verses(i,rhyme):
    print("The ants go marching",i+1,"by",i+1,"Hoorah! Hoorah!")
    print("The ants go marching",i+1,"by",i+1,"Hoorah! Hoorah!")
    print("The ants go marching",i+1,"by",i+1)
    print(rhyme)
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom!"*3)
    print("\n")

rhyme = ["The little one stops to suck his thump","The little one stops to tie his shoe","The little one stops to climb a tree","The little one stops to close the door","The little one stop to take a dive",
        "The little one stops to pick up sticks", "The little one stops to pray to heaven", "The little on stops to rollerskate","The little on stops to check the time"]
def main():
    for i in range(9):
        verses(i,rhyme[i])
    print("The ants go marching 10 by 10 Hoorah! Hoorah!")
    print("The ants go marching 10 by 10 Hoorah! Hoorah!")
    print("The ants go marching 10 by 10")
    print('The little one stops to shout\n"THE END!"')
main()
