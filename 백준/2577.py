a = int(input())
b = int(input())
c= int(input())
numstr = str(a*b*c)
nli = [0,0,0,0,0,0,0,0,0,0]
for i in numstr:
    nli[int(i)] += 1
for i in nli:
    print(i)