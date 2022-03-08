import sys
input = sys.stdin.readline

import collections
s,h = map(int, input().split())
q = collections.deque()
farm = []
time = [[0]*s]*h

for i in range(h):
    tmp = list(map(int,input().split()))
    for j, d in enumerate(tmp):
        if d == 1:
            q.append([i,j,0])
    farm.append(tmp)

dx, dy = [1,0,-1,0], [0,-1,0,1]

while q:
    i,j,d = q.popleft()
    d += 1
    for k in range(4):
        new_i, new_j = i+dx[k], j + dy[k]
        if new_i >= 0 and new_i < h and new_j >=0 and new_j < s:
            if farm[new_i][new_j] == 0:
                farm[new_i][new_j] = d
                time[new_i][new_j] = d
                q.append([new_i, new_j, d])

max = -1
signal = 0
for i in range(h):
    for j in range(s):
        if farm[i][j] == 0:
            signal = 1
            break
        if time[i][j]> max:
            max = time[i][j]
    if signal:
        max = -1
        break
print(max)