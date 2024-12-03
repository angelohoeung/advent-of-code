from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read()

import re

sumProd = 0
pattern = r"mul\((\d+),(\d+)\)"
mul = True
tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", lines)

for token in tokens:
    if token == "do()":
        mul = True
    elif token == "don't()":
        mul = False
    elif mul and (match := re.match(pattern, token)):
        num1, num2 = int(match.group(1)), int(match.group(2))
        sumProd += num1 * num2

print(sumProd)
