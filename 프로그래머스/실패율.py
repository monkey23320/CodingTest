def solution(N, stages):
    members = len(stages)
    answer = []
    for i in range(1, N + 1):
        count = stages.count(i)
        if members == 0:
            fail = 0
        else:
            fail = count / members
        answer.append((i, fail))
        members -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in answer]
    return answer