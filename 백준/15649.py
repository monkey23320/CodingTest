import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = [False] * (n + 1)

cnt = 0
printer = []

def print_num(cnt):
    if cnt == m:
        for i in printer:
            print(i, end=' ')
        print()
        return
    for i in range(1, n + 1):
        if num[i] == False:
            num[i] = True
            cnt += 1
            printer.append(i)
            print_num(cnt)
            printer.pop(-1)
            cnt -= 1
            num[i] = False

print_num(cnt)