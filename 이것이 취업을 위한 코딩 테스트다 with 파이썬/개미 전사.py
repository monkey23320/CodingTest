n = int(input())
food = list(map(int, input().split()))

table = [0] * n

table[0] = food[0]
table[1] = max(food[0], food[1])
for i in range(2,n):
    table[i] = max(table[i-1], table[i-2] + food[i])

print(max(table))