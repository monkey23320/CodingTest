def solution(n):
    answer = 0
    ternary = ''
    while n >= 3:
        t = n % 3
        n = n // 3
        ternary = str(t) + ternary
    ternary = str(n) + ternary

    for i, v in enumerate(ternary):
        answer += int(v) * (3 ** i)
    return answer