def solution(n, a, b):
    answer = 1

    while True:
        if abs((a // 2) - (b // 2)) == 1 and abs(a - b) == 1:
            break

        if a % 2 == 1:
            if a != 1:
                a = (a + 1) // 2
        else:
            a = a // 2

        if b % 2 == 1:
            if b != 1:
                b = (b + 1) // 2
        else:
            b = b // 2
        answer += 1

    return answer