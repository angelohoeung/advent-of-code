from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

orderRules = [line.split("|") for line in lines if "|" in line]
updates = [line.split(",") for line in lines if "," in line]

count = 0
valid = True
valids = []

for i in range(len(updates)):
    valid = True
    for j in range(len(updates[i])):
        for k in range(len(orderRules)):
            try:
                if updates[i][j] == orderRules[k][0] and updates[i].index(orderRules[k][1]) < j:
                    valid = False
            except:
                continue
    if valid:
        valids.append(updates[i])

for item in valids:
    count += int(item[(len(item) - 1) // 2])

print(count)
