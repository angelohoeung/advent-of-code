from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

orderRules = [line.split("|") for line in lines if "|" in line]
updates = [line.split(",") for line in lines if "," in line]

def checkValid(row):
    for i in range(len(row)):
        for j in range(len(orderRules)):
            try:
                if row[i] == orderRules[j][0] and row.index(orderRules[j][1]) < i:
                    return False
            except:
                continue
    return True

def fixRow(row):
    for i in range(len(row)):
        for j in range(len(orderRules)):
            try:
                if row[i] == orderRules[j][0] and row.index(orderRules[j][1]) < i:
                    temp = row[i]
                    row[i] = row[row.index(orderRules[j][1])]
                    row[row.index(orderRules[j][1])] = temp
            except:
                continue
    return row

count = 0
invalids = []

for update in updates:
    if not checkValid(update):
        invalids.append(update)

for i in range(len(invalids)):
    while not checkValid(invalids[i]):
        invalids[i] = fixRow(invalids[i])

for item in invalids:
    count += int(item[(len(item) - 1) // 2])

print(count)
