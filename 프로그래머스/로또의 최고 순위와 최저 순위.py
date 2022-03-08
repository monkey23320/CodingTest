def solution(lottos, win_nums):
    answer = []
    win = [6, 6, 5, 4, 3, 2, 1]
    zero = 0
    check = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            check += 1

    return [win[check + zero], win[check]]