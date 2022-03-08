num = int(input())
for i in range(num):
    a = list(map(int,input().split()))
    amean = sum(a[1:])/a[0]
    mon = 0
    for i in a[1:]:
        if i > amean:
            mon+=1
    print('%.3f' % (mon/a[0] * 100)  + '%')