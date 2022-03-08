n, m = map(int, input().split())
# row, column

pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ref = []
for _ in range(n):
    ref.append(list(map(int, list(input()))))

from collections import deque

count = 0
for i in range(n):
    for j in range(m):
        if ref[i][j] == 0:
            count += 1

            q = deque([(i, j)])
            ref[i][j] = 2

            while q:
                y, x = q.popleft()
                for k in range(4):
                    new_y, new_x = y + pos[k][0], x + pos[k][1]
                    if 0 <= new_y < n and 0 <= new_x < m and ref[new_y][new_x] == 0:
                        q.append((new_y, new_x))
                        ref[new_y][new_x] = 2

print(count)

