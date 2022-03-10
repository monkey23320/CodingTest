from collections import deque
def solution(s):
    stack = []
    new_s = deque(list(s))

    while new_s:
        c = new_s.popleft()
        if len(stack) == 0:
            stack.append(c)
            continue

        if c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0
    else:
        return 1

print(solution('cdcd'))