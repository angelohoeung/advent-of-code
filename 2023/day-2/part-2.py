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
total = 0

for line in lines:
    line = re.sub(r'Game \d+: ', '', line)
    dices = line.split('; ')
    dices = to_dict(dices)
    max_red = 0
    max_green = 0
    max_blue = 0
    for item in dices:
        max_red = max(max_red, item.get('red', 0))
        max_green = max(max_green, item.get('green', 0))
        max_blue = max(max_blue, item.get('blue', 0))
    total += max_red * max_green * max_blue
    
print(total)