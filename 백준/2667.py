from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
apart = []
check = [[False] * n for _ in range(n)]
for _ in range(n):
    apart.append(list(input().rstrip()))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
rooms = []
q = deque([])
cnt = 0
for i in range(n):
    for j in range(n):
        if apart[i][j] == '1' and check[i][j] == False:
            cnt += 1
            room = 1
            check[i][j] = True
            q.append((i, j))

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + di[k], y + dj[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if apart[nx][ny] == '1' and check[nx][ny] == False:
                            room += 1
                            check[nx][ny] = True
                            q.append((nx, ny))

            rooms.append(room)
            
# 문제 제대로 읽자
################
rooms.sort()
#################
print(cnt)
for room in rooms:
    print(room)
