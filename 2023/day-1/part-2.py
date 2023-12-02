from os.path import dirname
import re

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

digit_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

sum = 0

for line in lines:
    digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))', line)
    digits[0] = digit_dict.get(digits[0], digits[0])
    digits[-1] = digit_dict.get(digits[-1], digits[-1])
    sum += int(digits[0]) * 10 + int(digits[-1])

print(sum)