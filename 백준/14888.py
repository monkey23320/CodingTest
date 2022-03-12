import sys
input = sys.stdin.readline

from itertools import permutations

n = int(input())
numbers = list(map(int, input().rstrip().split()))
opers = list(map(int, input().rstrip().split()))
oper = ['+','-','*','/']

oper_list = []
for k in range(4):
    for i in range(opers[k]):
        oper_list.append(oper[k])

final_oper = list(set(list(permutations(oper_list, n-1))))

mins = 1000000000
maxs = -1000000000
for op in final_oper:

    tmp = numbers[0]
    for i in range(1,n):
        if op[i-1] == '+':
            tmp += numbers[i]
        elif op[i-1] == '-':
            tmp -= numbers[i]
        elif op[i-1] == '*':
            tmp *= numbers[i]
        else:
            if tmp < 0:
                tmp = -(-tmp // numbers[i])
            else:
                tmp = tmp//numbers[i]

    mins = min(tmp, mins)
    maxs = max(tmp, maxs)
print(maxs)
print(mins)
