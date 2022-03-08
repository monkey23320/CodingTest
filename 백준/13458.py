n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
only = 0
semi = 0
for num in a:
    if num > b:
        only += 1
        if (num-b) % c != 0:
            semi += int((num-b) // c) + 1
        else:
            semi += int((num-b) // c)
    else:
        only += 1
print(only+semi)