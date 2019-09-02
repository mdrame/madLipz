from random import shuffle

adjectives = list("blue") #explicite
nouns = list()

#colors list
colors = ['\033[95m', '\033[94m', '\033[92m','\033[93m','\033[91m','\033[0m' ]
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

def paragraph():


        print(f"""{colors[0]}My name is Mohammed. skfhsss
        fsfsffs
        sr
        fsrfgwrgjngksrhgwg
        wgwrgwkguwruhwrgw
        gwgwrguwhgwrgwrg
        wgwg""")




inputs()
paragraph()
