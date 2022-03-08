x = int(input())

table = [0] * (x+1)

def cal(target, table):
    total = 99999

    if target % 5 == 0:
        total = min(table[target//5] + 1, total)

    if target % 3 == 0:
        total = min(table[target//3] + 1, total)

    if target % 2 == 0:
        total = min(table[target//2] + 1, total)

    total = min(table[target - 1] + 1, total)

    return total


for i in range(2, x+1):
    table[i] = cal(i, table)

print(table[x])
