import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()
for i in range(n):
    inst = sys.stdin.readline().split()
    if inst[0] == 'push_back':
        d.append(int(inst[1]))
    elif inst[0] == 'push_front':
        d.appendleft(int(inst[1]))
    elif inst[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif inst[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif inst[0] == 'size':
        print(len(d))
    elif inst[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif inst[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])