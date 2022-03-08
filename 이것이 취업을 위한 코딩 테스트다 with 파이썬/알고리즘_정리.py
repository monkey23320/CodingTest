## DFS
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end= ' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
#
# visited = [False] * 9
# dfs(graph,1,visited)

## BFS
# from collections import deque
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#
#     visited[start]= True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
#
# visited = [False] * 9
# bfs(graph,1,visited)

## quicksort
# array = [5,7,9,0,3,1,6,2,4,8]
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# print(quick_sort(array))

## count sort
# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# count = [0] * (max(array) + 1)
#
# for i in range(len(array)):
#     count[array[i]] += 1
#
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end =' ')

## binary_search
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

## dijkstra
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n,m = map(int, input().split())
#
# start = int(input())
# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n +1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
# dijkstra(start)
#
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

## advanced dijkstra
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n,m = map(int,input().split())
#
# start = int(input())
#
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))
#
# def advanced_dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))
#
# advanced_dijkstra(start)
#
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print('INFINITY')
#     else:
#         print(distance[i])

## Floyd-Warshall
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
#
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a][b] = c
#
# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if graph[a][b] == INF:
#             print('INFINITY', end =' ')
#         else:
#             print(graph[a][b], end = ' ')
#     print()

## union
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b= find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int,input().split())
# parent = [0] * (v+1)
#
# for i in range(1,v+1):
#     parent[i] = i
#
# for i in range(e):
#     a,b = map(int, input().split())
#     union_parent(parent, a, b)

## kruskal
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent ,b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v+1)
#
# edges = []
# result = 0
# for i in range(v+1):
#     parent[i] = i
#
# for _ in range(e):
#     a, b, cost = map(int,input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(result)

## topology sort
# from collections import deque
#
# v,e = map(int,input().split())
#
# indegree = [0] * (v+1)
# graph = [[] for i in range(v+1)]
#
# for _ in range(e):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     indegree[b] += 1
#
# def topology_sort():
#     result = []
#     q = deque()
#
#     for i in range(1, v+1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
#     for i in result:
#         print(i, end=' ')
#
# topology_sort()