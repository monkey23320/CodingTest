def solution(dartResult):
    answer = 0
    region = {'S' : 1, 'D' : 2, 'T':3}
    score = [0,0,0,0]
    index = 0
    i = 0
    while i < len(dartResult):
        if '0' <= dartResult[i] <= '9':
            index += 1
            if dartResult[i+1] == '0':
                score[index] += int(dartResult[i:i+2])
                i += 1
            else:
                score[index] += int(dartResult[i])
            i += 1
        elif dartResult[i] in ['S', 'D', 'T']:
            score[index] = score[index] ** region[dartResult[i]]
            i += 1
        else:
            if dartResult[i] == '*':
                score[index-1] *= 2
                score[index] *= 2
            else:
                score[index] *= -1
            i+= 1
    return sum(score)