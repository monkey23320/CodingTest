test = int(input())
for i in range(1, test+1):
    a, b = input().split()
    print("Case #{}: {} + {} = {}".format(i, a, b, int(a) + int(b)))