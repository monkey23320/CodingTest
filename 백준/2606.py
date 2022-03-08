import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
virus = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

m = int(input())
for _ in range(m):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)
q = deque()
q.append(1)
virus[1] = True

cnt = 0
while q:
    now = q.popleft()
    for c in graph[now]:
        if virus[c] == False:
            virus[c] = True
            cnt += 1
            q.append(c)

print(cnt)