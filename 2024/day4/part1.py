from os.path import dirname

with open(f"{dirname(__file__)}/input.txt", "r") as file:
    rows = file.read().splitlines()

count = 0

'''
X
 M
  A
   S
'''
for i in range (len(rows) - 3):
    for j in range(len(rows[0]) - 3):
        if rows[i][j] == 'X' and rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S':
            count += 1

'''
   X
  M
 A
S
'''
for i in range (len(rows) - 3):
    for j in range(3, len(rows[0])):
        if rows[i][j] == 'X' and rows[i+1][j-1] == 'M' and rows[i+2][j-2] == 'A' and rows[i+3][j-3] == 'S':
            count += 1

'''
   S
  A
 M
X
'''
for i in range (len(rows) - 3):
    for j in range(3, len(rows[0])):
        if rows[i][j] == 'S' and rows[i+1][j-1] == 'A' and rows[i+2][j-2] == 'M' and rows[i+3][j-3] == 'X':
            count += 1

'''
S
 A
  M
   X
'''
for i in range (len(rows) - 3):
    for j in range(len(rows[0]) - 3):
        if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+3][j+3] == 'X':
            count += 1

'''
X
M
A
S
'''
for i in range (len(rows) - 3):
    for j in range(len(rows[0])):
        if rows[i][j] == 'X' and rows[i+1][j] == 'M' and rows[i+2][j] == 'A' and rows[i+3][j] == 'S':
            count += 1

'''
S
A
M
X
'''
for i in range (len(rows) - 3):
    for j in range(len(rows[0])):
        if rows[i][j] == 'S' and rows[i+1][j] == 'A' and rows[i+2][j] == 'M' and rows[i+3][j] == 'X':
            count += 1

for row in rows:
    count += row.count('XMAS') + row.count('SAMX')

print(count)
