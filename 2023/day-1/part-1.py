from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

sum = 0

for line in lines:
    digits = [int(char) for char in line if char.isdigit()]
    sum += digits[0] * 10 + digits[-1]

print(sum)