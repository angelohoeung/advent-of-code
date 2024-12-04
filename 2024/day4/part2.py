from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    rows = file.read().splitlines()

count = 0

'''
M M
 A
S S
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        if rows[i][j] == 'M' and rows[i][j+2] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'S' and rows[i+2][j+2] == 'S':
            count += 1

'''
M S
 A
M S
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        if rows[i][j] == 'M' and rows[i][j+2] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'M' and rows[i+2][j+2] == 'S':
            count += 1

'''
S S
 A
M M
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        if rows[i][j] == 'S' and rows[i][j+2] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'M' and rows[i+2][j+2] == 'M':
            count += 1

'''
S M
 A
S M
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        if rows[i][j] == 'S' and rows[i][j+2] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'S' and rows[i+2][j+2] == 'M':
            count += 1

print(count)
