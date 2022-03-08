num = int(input())
a = list()
for i in range(num):
    a.append(input())
for b in a:
    score = 0
    tmps = 0
    for i in b:
        if i == 'O':
            tmps += 1
            score += tmps
        else:
            tmps = 0
    print(score)