import collections
def solution(numbers, target):
    answer = 0
    q = collections.deque()
    n = len(numbers)
    value = 0
    q.append([value + numbers[0], 0])
    q.append([value - numbers[0], 0])
    while q:
        value, i = q.popleft()
        i += 1
        if i < n:
            q.append([value + numbers[i], i])
            q.append([value - numbers[i], i])
        else:
            if value == target:
                answer += 1
    return answer