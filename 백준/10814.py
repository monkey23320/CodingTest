import sys

input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    info = list(input().split())
    result.append([i, int(info[0]), info[1]])

result.sort(key=lambda x: (x[1], x[0]))

for info in result:
    print(info[1],info[2])
