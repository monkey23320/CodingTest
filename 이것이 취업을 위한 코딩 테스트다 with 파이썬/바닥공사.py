n = int(input())
table = [0,1,3,]
# An = An-1 + 2 * An-2

for i in range(3,n+1):
    table.append(table[i-1] + (2*table[i-2]))

print(table[n] % 796796)
