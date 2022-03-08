def solution(n):
    answer = ''
    tmp = 0
    sum_124 = 0
    for i in range(1, 20):
        if sum_124 + 3 ** i >= n:
            tmp = i
            break
        sum_124 += 3 ** i
    n -= sum_124

    while tmp > 0:
        if n - (3 ** (tmp - 1)) <= 0:
            answer += '1'
            tmp -= 1
            continue

        if n - 2 * (3 ** (tmp - 1)) <= 0:
            answer += '2'
            n -= 3 ** (tmp - 1)
            tmp -= 1
            continue

        if n - 3 * (3 ** (tmp - 1)) <= 0:
            answer += '4'
            n -= 2 * (3 ** (tmp - 1))
            tmp -= 1
            continue

    return answer