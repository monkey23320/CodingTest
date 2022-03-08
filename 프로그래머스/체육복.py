def solution(n, lost, reserve):
    answer = 0
    judge = [1] * (n + 2)
    judge[0] = 0
    judge[n + 1] = 0
    for s in reserve:
        judge[s] += 1
    for s in lost:
        judge[s] -= 1

    for i in range(1, n + 1):
        if judge[i] >= 1:
            answer += 1
        else:
            if judge[i - 1] > 1:
                judge[i - 1] -= 1
                judge[i] += 1
                answer += 1
            elif judge[i + 1] > 1:
                judge[i + 1] -= 1
                judge[i] += 1
                answer += 1
    return answer