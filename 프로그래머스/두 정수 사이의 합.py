def solution(a, b):
    answer = 0
    check = abs(a-b) + 1
    if check % 2 == 1:
        answer = (a+b) * (abs(a-b)//2) + (a+b)//2
    else:
        answer = (a+b) * (check//2)
    return answer