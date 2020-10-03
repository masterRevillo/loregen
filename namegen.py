import sys
import random

def generateCreatureName():
    return generateName(3, 6, 'creature.txt', 'Creature')

def generateDwarfName():
    return generateName(2, 4, 'dwarf.txt', 'Dwarf')

def generateElfName():
    return generateName(3, 5, 'elf.txt', 'Elf')

def generateName(minSyllables, maxSyllables, sourceFile, species):
    f = open(sourceFile, 'r')
    contents = f.read()
    sourceSylables = contents.split("\n")
    name = ""
    numSyllables = random.randint(minSyllables,maxSyllables)
    for j in range(0,numSyllables):
        sy = sourceSylables[random.randint(0,len(sourceSylables)-1)]
        name += sy
    return name.title() + ' the ' + species