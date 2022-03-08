import sys
n = int(input())
store = list(map(int, sys.stdin.readline().rstrip().split()))
store.sort()

m = int(input())
find = list(map(int, sys.stdin.readline().rstrip().split()))

def bs(store, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if store[mid] == target:
            return True
        if store[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for number in find:
    if bs(store, 0, n-1, number):
        print('yes' , end = ' ')
    else:
        print('no', end = ' ')

# using radix OR using set

# radix = [0] * 1000001
# store = list(map(int, input().split()))
# for i in store:
#   radix[i] += 1
# for i in find:
#   if radix[i] == 1:
#       print('yes')

# store = set(map(int, input().split()))
# for i in find:
#   if i in store:
#       print('yes)