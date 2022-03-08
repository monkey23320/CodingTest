def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

n, m = map(int, input().split())
stu = [0] * (n+1)

for i in range(n+1):
    stu[i] = i

for _ in range(m):
    com, a, b = map(int, input().split())
    if com:
        if stu[a] == stu[b]:
            print("YES")
        else:
            print("NO")

    else:
        pa = find_parent(stu, a)
        pb = find_parent(stu, b)
        if pa < pb:
            stu[b] = pa
        else:
            stu[a] = pb