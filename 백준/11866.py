import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())
l = deque(range(1,a+1))
print('<', end='')
while True:
    if len(l) == 1: break
    l.rotate(1-b)
    print(l.popleft(), end=', ')
print(l[0], end='>')