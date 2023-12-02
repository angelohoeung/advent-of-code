from os.path import dirname
import re

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

def to_dict(data):
    color_list = []
    for item in data:
        color_dict = {}
        pairs = item.split(', ')
        for pair in pairs:
            quantity, color = pair.split(' ')
            quantity = int(quantity)
            color_dict[color] = quantity
        color_list.append(color_dict)
    return color_list

red = 12
green = 13
blue = 14
dices = []
count = 1
total = 0

for line in lines:
    line = re.sub(r'Game \d+: ', '', line)
    dices = line.split('; ')
    dices = to_dict(dices)
    for i, item in enumerate(dices):
        if item.get('red', 0) > red or item.get('green', 0) > green or item.get('blue', 0) > blue:
            break
        total += count if i == len(dices) - 1 else 0
    count += 1
    
print(total)