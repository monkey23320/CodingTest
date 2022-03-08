n = int(input())
coins = list(map(int, input().split()))
coins.sort()
"""
target = 1
for x in coins:
    if target < x:
        break
    target += x

print(target)
"""
check = [False] * (sum(coins) + 1)

for i in range(len(coins)):
    now = 0
    for j in range(i, len(coins)):
        now += coins[j]
        check[now] = True

for i in range(1, len(check)):
    if not check[i]:
        print(i)
        break