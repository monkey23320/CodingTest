import sys

l = list()

n = int(sys.stdin.readline())
for i in range(n):
    inst = int(sys.stdin.readline())
    if inst == 0:
        l.pop()
    else:
        l.append(inst)
print(sum(l))