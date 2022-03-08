import sys

input = sys.stdin.readline

h, m = map(int, input().split())
load = int(input())

print((h + (m + load) // 60) % 24, (m + load) % 60)
