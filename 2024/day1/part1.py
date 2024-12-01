from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()
lefts = []
rights = []
total = 0

for line in lines:
    thing = line.split()
    lefts.append(int(thing[0]))
    rights.append(int(thing[1]))

lefts.sort()
rights.sort()
for num in zip(lefts, rights):
    total += abs(num[0] - num[1])

print(total)
