import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
d = deque(range(1,n+1))
for i in l:
    while True:
        if i == d[0]:
            d.popleft()
            break
        ix = d.index(i)
        if len(d) - ix >= ix:
            d.rotate(-ix)
            cnt += ix
        else:
            d.rotate(len(d) - ix )
            cnt += len(d) - ix
print(cnt)