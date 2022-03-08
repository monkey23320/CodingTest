a1, b1 = input().split()
a2 = ''
b2 = ''
for i in a1:
    a2 = i + a2
for i in b1:
    b2 = i + b2
a2 = int(a2)
b2 = int(b2)
if (a2 > b2):
    print(a2)
else:
    print(b2)

