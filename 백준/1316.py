num = int(input())
n = 0
for i in range(num):
    a = input()
    el = list()
    c = '?'
    signal = 1
    for j in range(len(a)):
        if c != a[j]:
            if a[j] not in el:
                el.append(a[j])
                c = a[j]
            else:
                signal = 0
                break
    if signal:
        n += 1
print(n)