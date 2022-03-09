def solution(s):
    s = s[2:-2]
    ns = s.split('},{')
    fs = [list(map(int, x.split(','))) for x in ns]
    fs.sort(key = lambda x : len(x))
    answer = []
    for x in fs:
        for i in set(x) - set(answer):
            answer.append(i)

    return answer
