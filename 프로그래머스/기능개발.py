def solution(progresses, speeds):
    answer = []
    end = len(progresses)
    index = 0

    while index < end:
        reserve = 100 - progresses[index]
        days, check = reserve // speeds[index], reserve % speeds[index]
        if check != 0:
            days += 1

        for i in range(index, end):
            progresses[i] += speeds[i] * days

        count = 0
        while index < end and progresses[index] >= 100:
            count += 1
            index += 1
        answer.append(count)
    return answer