import sys
import random
import namegen

print 'Argument List:', str(sys.argv)

if (len(sys.argv) != 2):
    print("Usage:")
    print("python loregen.py <number of years>")
    exit()

numYears = int(sys.argv[1])

f = open('events.txt', 'r')
contents = f.read()

events = contents.split("\n")
history = []

for i in range(1,numYears+1):
    eventNum = random.randint(0,len(events)-1)
    event = events[eventNum]
    event =event.replace('{year}', str(i))
    if ('{dwarfName}' in event):
        event = event.replace('{dwarfName}', namegen.generateDwarfName())

    if ('{elfName}' in event):
        event = event.replace('{elfName}', namegen.generateElfName())

    if ('{creatureName}' in event):
        event = event.replace('{creatureName}', namegen.generateCreatureName())
    history.append(event)

print("Generated history:")
for i in history:
    print(i)
