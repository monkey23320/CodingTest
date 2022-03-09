from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    nums = deque([])
    opers = deque([])
    oper =[]
    tmp = ''
    for c in expression:
        if c in ['+','-','*']:
            oper.append(c)
            opers.append(c)
            nums.append(int(tmp))
            tmp = ''
        else:
            tmp += c
    nums.append(int(tmp))
    oper = list(set(oper))

    priority = list(permutations(oper, len(oper)))

    for p in priority:
        nums_tmp = nums.copy()
        opers_tmp = opers.copy()
        nums_stack = deque([nums_tmp.popleft()])
        opers_stack = deque([])
        for i in range(len(oper)):
            for _ in range(len(opers_tmp)):
                num = nums_tmp.popleft()
                op = opers_tmp.popleft()
                if op == p[i]:
                    pnum = nums_stack.pop()
                    if op == '+':
                        nums_stack.append(pnum+num)
                    elif op == '*':
                        nums_stack.append(pnum * num)
                    else:
                        nums_stack.append(pnum - num)
                else:
                    nums_stack.append(num)
                    opers_stack.append(op)
            nums_tmp = nums_stack
            opers_tmp = opers_stack
            nums_stack = deque([nums_tmp.popleft()])
            opers_stack = deque([])
        answer = max(answer, abs(nums_stack[0]))



    return answer

print(solution("50*6-3*2"))