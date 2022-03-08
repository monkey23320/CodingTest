def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    count = [0, 0, 0]

    for i, sc in enumerate(answers):
        if sc == first[i]:
            count[0] += 1
        if sc == second[i]:
            count[1] += 1
        if sc == third[i]:
            count[2] += 1

    high = max(count)
    for i, c in enumerate(count):
        if high == c:
            answer.append(i + 1)
    return answer