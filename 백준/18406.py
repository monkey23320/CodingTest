num = list(map(int, list(input())))
left = num[:len(num)//2]
right = num[len(num)//2:]
if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')