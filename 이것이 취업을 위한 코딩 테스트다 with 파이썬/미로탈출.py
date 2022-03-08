n, m = map(int, input().split())

from collections import deque
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

pos = [(1,0),(0,1),(-1,0),(0,-1)]
q = deque([(0,0)])
while q:
    y,x = q.popleft()
    for i in range(4):
        ny, nx = y + pos[i][0], x + pos[i][1]
        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
            maps[ny][nx] = maps[y][x] + 1
            q.append((ny, nx))

print(maps[n-1][m-1])