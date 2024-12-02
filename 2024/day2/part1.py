from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

safeNum = 0

for line in lines:
    row = list(map(int, line.split()))
    safe = True
    if row != sorted(row) and row != sorted(row, reverse=True):
        safe = False
        continue
    for i in range(len(row) - 1):
        if not (1 <= abs(row[i] - row[i + 1]) <= 3):
            safe = False
            break
    if safe:
        safeNum += 1

print(safeNum)
