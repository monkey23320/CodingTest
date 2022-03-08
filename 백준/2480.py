import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

# rule 1
if a == b and b == c:
    print(10000 + (a*1000))

else:
    # rule 2
    if a == b:
        print(1000 + (a*100))
    elif a == c:
        print(1000 + (a * 100))
    elif b == c:
        print(1000 + (b * 100))

    # rule 3
    else:
        print(max(a,b,c) * 100)
