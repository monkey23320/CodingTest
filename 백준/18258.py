import sys
from collections import deque

x = int(sys.stdin.readline())
l = deque()

for i in range(x):
    inst = sys.stdin.readline().split()
    if inst[0] == 'push':
        l.append(int(inst[1]))
        continue
    if inst[0] == 'pop':
        if len(l) == 0:
            print(-1)
            continue
        print(l.popleft())
        continue
    if inst[0] == 'size':
        print(len(l))
        continue
    if inst[0] == 'empty':
        if len(l) == 0:
            print(1)
            continue
        print(0)
        continue
    if inst[0] == 'front':
        if len(l) == 0:
            print(-1)
            continue
        print(l[0])
        continue
    if inst[0] == 'back':
        if len(l) == 0:
            print(-1)
            continue
        print(l[-1])