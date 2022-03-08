n = int(input())
member = list(map(int, input().split()))
# 가장 작은 순서대로 넣으면 최대 그룹수가 나옴
"""
member.sort()
result = 0
count = 0
for i in member:
    count += 1
    if count >= i:
        result += 1
        count = 0
"""
member.sort(reverse=True)

group = 0

index = 0
while index < n:
    count = 0
    cir = 0
    first = index
    while first <= n - 1:
        if first + member[first] - 1 <= n - 1:
            count += 1
            first += member[first]

    if count > group:
        group = count
    index += 1

print(group)


