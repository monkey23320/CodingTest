n = int(input())
k = 1
for i in range(2,n+1):
    k *= i

l = list(str(k))[::-1]
answer = 0

for num in l:
    if num != '0':
        print(answer)
        break
    answer += 1