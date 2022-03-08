import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())
words = list(set(words))
words.sort(key = lambda x : (len(x), x))

for word in words:
    print(word)