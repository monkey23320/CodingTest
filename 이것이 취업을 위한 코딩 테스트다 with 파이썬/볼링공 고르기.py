n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = 0
weights = [0] * (m+1)
for x in balls:
    weights[x] += 1

for cnt in weights[1:]:
    # n -= cnt
    # result += cnt * n
    result += (cnt * (n - cnt))

# print(result
print(result // 2)