def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

group = [0] * (n+1)

for i in range(n+1):
    group[i] = i

q = []

for _ in range(m):
    a,b,cost = map(int, input().split())
    q.append((cost, a, b))

q.sort()

total = 0
last = 0
for c in q:
    cost, a, b = c
    if find_parent(group, a) != find_parent(group, b):
        print(a, b, cost)
        union(group, a, b)
        total += cost
        last = cost

print(total - last)