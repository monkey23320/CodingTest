import sys
from collections import deque

n = int(sys.stdin.readline())
for i in range(n):
    d, idx = map(int, sys.stdin.readline().split())
    pri = deque(map(int, sys.stdin.readline().split()))
    prt = deque(range(d))
    tmp = list()
    while True:
        if max(pri) == pri[prt.index(idx)]:
            cnt = 0
            for i in range(prt.index(idx)):
                if pri[i] == pri[prt.index(idx)]:
                    cnt += 1
            print(len(tmp) + cnt + 1)
            break
        tmpi = pri.index(max(pri))
        pri.rotate(-(tmpi))
        prt.rotate(-(tmpi))
        tmp.append(pri.popleft())
        prt.popleft()