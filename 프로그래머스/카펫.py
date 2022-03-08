def solution(brown, yellow):
    answer = []
    import math
    for i in range(1, math.floor(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if (i * 2) + ((yellow // i) * 2) + 4 == brown:
                answer.append((yellow // i) + 2)
                answer.append(i+2)
                break
    return answer