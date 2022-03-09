import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(input())

for _ in range(n):
    y, x, t = map(int, input().split())
    farm = [[0] * y for _ in range(x)]
    for _ in range(t):
        i, j = map(int, input().split())
        farm[j][i] = 1
    cnt = 0
    q = deque([])
    for i in range(x):
        for j in range(y):
            if farm[i][j] == 1:
                cnt += 1
                farm[i][j] = 0
                q.append((i, j))
                while q:
                    tx, ty = q.popleft()
                    for k in range(4):
                        nx, ny = tx + dx[k], ty + dy[k]
                        if 0 <= nx < x and 0 <= ny < y:
                            if farm[nx][ny] == 1:
                                farm[nx][ny] = 0
                                q.append((nx, ny))

    print(cnt)
