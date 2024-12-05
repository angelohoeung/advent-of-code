from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

orderRules = [line.split("|") for line in lines if "|" in line]
updates = [line.split(",") for line in lines if "," in line]

count = 0
valid = True
invalids = []
incorrNums = []

for i in range(len(updates)):
    valid = True
    for j in range(len(updates[i])):
        for k in range(len(orderRules)):
            try:
                if updates[i][j] == orderRules[k][0] and updates[i].index(orderRules[k][1]) < j:
                    valid = False
                    break
            except:
                continue
    if not valid:
        invalids.append(updates[i])

for idk in range(25):
    for i in range(len(invalids)):
        for j in range(len(invalids[i])):
            for k in range(len(orderRules)):
                try:
                    if invalids[i][j] == orderRules[k][0] and invalids[i].index(orderRules[k][1]) < j:
                        temp = invalids[i][j]
                        invalids[i][j] = invalids[i][invalids[i].index(orderRules[k][1])]
                        invalids[i][invalids[i].index(orderRules[k][1])] = temp
                except:
                    continue

for item in invalids:
    count += int(item[(len(item) - 1) // 2])

print(count)
