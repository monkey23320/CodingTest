import sys
input = sys.stdin.readline

import heapq

INF = int(1e9)
v, e = map(int,input().split())
distance = [INF] * (v+1)
graph = [[]for _ in range(v+1)]

start = int(input())

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, i = heapq.heappop(q)

    if dist > distance[i]:
        continue
    for x in graph[i]:
        cost = dist + x[1]
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(q,(cost, x[0]))

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])