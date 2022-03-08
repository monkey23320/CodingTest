def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        check = format(a | b, 'b')
        if len(check) != n:
            check = '0' * (n - len(check)) + check
        answer.append((check.replace('1', '#')).replace('0', ' '))

    return answer