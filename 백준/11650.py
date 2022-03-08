import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = []
for _ in range(n):
    a,b = map(int, input().rstrip().split())
    numbers.append((a,b))

numbers.sort(key = lambda x : (x[0], x[1]))

for i in numbers:
    print(i[0],i[1])