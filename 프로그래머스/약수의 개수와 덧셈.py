def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if (num**0.5).is_integer():
            answer -= num
        else:
            answer += num
    return answer