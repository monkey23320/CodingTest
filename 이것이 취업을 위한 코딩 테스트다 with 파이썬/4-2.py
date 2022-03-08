n = int(input())
# 1분에 3이 있는 경우 : 3, 13, 23, 3x, 43, 53 - 15
# 1시간에 3이 있는 경우 : 15 * 60 + 45 * 15 = 900 + 675 = 1575
# 전체 시간중 3이 포함 : 3,13,23

if n == 23:
    print(3*3600 + 21*1575)
elif 13 <= n < 23:
    print(2*3600 + (n-1)*1575)
elif 3 <= n < 13:
    print(3600 + (n) * 1575)
else:
    print((n+1) * 1575)