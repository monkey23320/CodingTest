import sys
import math

n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    # 동심원
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        smaller = r1
        bigger = r2
        if smaller > bigger:
            smaller = r2
            bigger = r1
        # 안만나는 경우
        if bigger > distance + smaller or distance > bigger + smaller:
            print(0)
        # 한점
        elif bigger == distance + smaller or distance == bigger + smaller:
            print(1)
        else:
            print(2)