N = int(input())
coin = [500, 100, 50, 10]
count = 0
for c in coin:
    count += N // c
    N = N % c
print(count)
