INF = int(1e9)

n, m = map(int, input().split())
maps = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            maps[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    maps[a][b] = 1
    maps[b][a] = 1

x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            maps[b][c] = min(maps[b][c], maps[b][a] + maps[a][c])

result = maps[1][k] + maps[k][x]

if result >= INF:
    print("-1")

else:
    print(result)