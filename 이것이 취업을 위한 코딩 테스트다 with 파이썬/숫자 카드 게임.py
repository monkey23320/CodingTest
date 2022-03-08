n, m = map(int, input().split())
mins = []
# result = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    mins.append(min(nums))
    # min_value = min(nums)
    # result = max(result, min_value)

print(max(mins))
# print(result)
