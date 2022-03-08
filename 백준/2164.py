import sys
from collections import deque
n = int(sys.stdin.readline())

l = deque(range(1,n+1))
while(True):
    if len(l) == 1: break
    l.popleft()
    l.append(l.popleft())
print(l[0])