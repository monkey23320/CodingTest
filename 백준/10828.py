import sys

l = list()
n = int(sys.stdin.readline())
for i in range(n):
    inst = list(sys.stdin.readline().split())
    if inst[0] == 'push':
        l.append(int(inst[1]))
    elif inst[0] == 'top':
        if len(l) == 0: print(-1)
        else: print(l[-1])
    elif inst[0] == 'size':
        print(len(l))
    elif inst[0] == 'empty':
        if len(l)  == 0: print(1)
        else: print(0)
    elif inst[0] == 'pop':
        if len(l) == 0: print(-1)
        else: print(l.pop())