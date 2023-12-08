from os.path import dirname
import re

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

total = 0

for line in lines:
    line = re.sub(r'Card +\d+: ', '', line)
    cards = line.split(' | ')
    cards[0] = list(cards[0].split())
    cards[1] = list(cards[1].split())
    matches = sum(nums in cards[0] for nums in cards[1])
    total += 2**(matches - 1) if matches > 0 else 0

print(total)