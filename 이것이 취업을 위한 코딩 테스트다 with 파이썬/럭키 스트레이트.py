lucky = input()
l = len(lucky)
left, right = list(map(int, lucky[:l//2])), list(map(int, lucky[l//2:]))
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")