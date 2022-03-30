from collections import deque
def solution(msg):
    answer = []
    dictionary = {}
    for i in range(ord('A'), ord('Z') + 1):
        dictionary[chr(i)] = i - ord('A') + 1
    new = 27
    m = deque(list(msg))

    while m:
        new_msg = m.popleft()
        while m:
            if new_msg not in dictionary:
                break
            new_msg += m.popleft()

        if new_msg not in dictionary:
            dictionary[new_msg] = new
            new += 1
            m.appendleft(new_msg[-1])
            answer.append(dictionary[new_msg[:-1]])
        else:
            answer.append(dictionary[new_msg])

    return answer


print(solution('ABABABABABABABAB'))
