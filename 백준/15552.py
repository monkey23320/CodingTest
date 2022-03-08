import sys

test = int(sys.stdin.readline().rstrip())
for i in range(test):
    a, b = (sys.stdin.readline().rstrip()).split()
    print(int(a) + int(b))