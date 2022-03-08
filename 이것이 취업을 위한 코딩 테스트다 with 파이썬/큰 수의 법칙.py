n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

if nums[-1] == nums[-2]:
    print(nums[-1] * m)
else:
    print(((m // (k+1)) * ((nums[-1] * k) + nums[-2])) + (nums[-1] * (m % (k+1))))
