import sys
input = sys.stdin.readline

numbers = [0] * 10001

n = int(input())

for _ in range(n):
    numbers[int(input())] += 1

for i in range(1, 10001):
    for _ in range(numbers[i]):
        print(i)