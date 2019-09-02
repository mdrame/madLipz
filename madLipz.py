from random import shuffle

adjectives = list() #explicite
nouns = list()


#colors list
colors = ['\033[95m', '\033[94m', '\033[92m','\033[93m','\033[91m' ]
shuffle(colors) #randomze list here
#print(colors) test



def inputs():

    nouns.append(input("Noun: "))
    adjectives.append(input("Ajective: "))
    nouns.append(input("Noun: "))
    adjectives.append(input("Ajective: "))
    adjectives.append(input("Ajective: "))
    nouns.append(input("Noun: "))
    adjectives.append(input("Ajective: "))
    nouns.append(input("Noun: "))
    adjectives.append(input("Ajective: "))
    nouns.append(input("Noun: "))

    print(nouns)
    print(adjectives)

def paragraph():


    print(f"{colors[0]} {nouns[0]} is the")
    print(f"{adjectives[0]} teacher in the world.")
    print(f"{nouns[1]} is {adjectives[1]} and")
    print(f"{adjectives[2]} {nouns[2]} makes:")
    print(f"learning {adjectives[3]}, especially in")
    print(f"{nouns[3]}. school is {adjectives[4]},")
    print(f"because of {nouns[4]}! ")




inputs()
paragraph()
