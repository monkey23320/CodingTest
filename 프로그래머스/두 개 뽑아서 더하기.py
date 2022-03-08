def solution(numbers):
    answer = []
    from itertools import combinations as c
    for i, j in list(c(numbers, 2)):
        if i + j not in answer:
            answer.append(i + j)

    return sorted(answer)