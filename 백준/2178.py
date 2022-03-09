import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, list(input().rstrip()))))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
check = [[False] * m for _ in range(n)]

from collections import deque

q = deque([])
q.append((0, 0))

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

print(maze[n - 1][m - 1])
