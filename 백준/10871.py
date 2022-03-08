test, base = map(int,input().split())
a = input().split()
for i in a:
    if(int(i) < base):
        print(int(i), end=' ')
