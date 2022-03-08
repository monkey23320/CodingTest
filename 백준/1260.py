import sys
input = sys.stdin.readline
from collections import deque
n,m,start = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,d = map(int,input().split())
    graph[s].append(d)
    graph[d].append(s)


def dfs(visited, start):
    visited[start] = True
    print(start, end = ' ')
    for i in sorted(graph[start]):
        if visited[i] == False:
            dfs(visited,i)

def bfs(visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        next = q.popleft()
        print(next, end= ' ')
        for i in sorted(graph[next]):
            if visited[i] == False:
                visited[i] = True
                q.append(i)

dfs(visited, start)
print()
visited = [False] * (n+1)
bfs(visited, start)