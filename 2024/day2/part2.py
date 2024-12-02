from os.path import dirname

def is_safe(row):
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row) - 1):
            if not (1 <= abs(row[i] - row[i + 1]) <= 3):
                return False
        return True
    return False

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

safeNum = 0

for line in lines:
    row = list(map(int, line.split()))
    if is_safe(row):
        safeNum += 1
    else:
        for i in range(len(row)):
            new_row = row[:i] + row[i+1:]
            if is_safe(new_row):
                safeNum += 1
                break

print(safeNum)
