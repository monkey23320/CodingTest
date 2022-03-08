def solution(num):
    count = 0
    while count < 499:
        if num == 1:
            return count
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1

    return -1