from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read()

import re

sumProd = 0
pattern = r"mul\((\d+),(\d+)\)"
things = re.findall(pattern, lines)

for match in things:
    sumProd += int(match[0]) * int(match[1])

print(sumProd)
