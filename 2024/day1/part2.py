from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()
lefts = []
rights = []
simScore = 0

for line in lines:
    thing = line.split()
    lefts.append(int(thing[0]))
    rights.append(int(thing[1]))

for left in lefts:
    simScore += left * rights.count(left)

print(simScore)
