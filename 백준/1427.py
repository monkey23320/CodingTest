import sys
input = sys.stdin.readline

numbers = list(map(int,list(input().rstrip())))
numbers.sort(reverse=True)

print(''.join(map(str, numbers)))