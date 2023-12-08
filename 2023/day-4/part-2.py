from os.path import dirname
import re

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

num_matches = []

for line in lines:
    line = re.sub(r'Card +\d+: ', '', line)
    cards = line.split(' | ')
    cards[0] = list(cards[0].split())
    cards[1] = list(cards[1].split())
    num_matches.append(sum(nums in cards[0] for nums in cards[1]))

instances = [1 for i in num_matches]
for i, num in enumerate(num_matches):
    for j in range(i + 1, i + num + 1):
        instances[j] += instances[i]

print(sum(instances))