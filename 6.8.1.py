#6.8.1.py
# This programprints the lyrics to "Old McDonald" childrens song

def chorus():
    print("Old McDonald had a farm, Ee-igh, Ee-igh, Oh!")

def farm(animal, noise):
    print("On that farm he had a",animal+", Ee-igh, Ee-igh, Oh!")
    print("With a",noise+",",noise,"here and a",noise+",",noise, "there" )
    print("Here a",noise+", there a",noise+", everywhere a", noise, noise)

def main():
    print()
    chorus()
    farm("cow", "moo")
    chorus()
    print()
    chorus()
    farm("cat", "meow")
    chorus()
    print()
    chorus()
    farm("dog", "bark")
    chorus()
    print()
    chorus()
    farm("crow", "caw")
    chorus()
    print()
    chorus()
    farm("horse", "neigh")
    chorus()
main()
