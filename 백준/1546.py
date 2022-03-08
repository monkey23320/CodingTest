num= int(input())
a = list(map(int, input().split()))
msc= max(a)
for i in range(len(a)):
    a[i] = a[i] / msc * 100
print(sum(a)/num)