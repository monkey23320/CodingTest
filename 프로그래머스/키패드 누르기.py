def solution(numbers, hand):
    answer = ''
    pad = [[4, 2], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 3]]
    now_l = 10
    now_r = 11
    for num in numbers:
        if num in [1, 4, 7]:
            now_l = num
            answer += 'L'
        elif num in [3, 6, 9]:
            now_r = num
            answer += 'R'
        else:
            if abs(pad[now_r][0] - pad[num][0]) + abs(pad[now_r][1] - pad[num][1]) < abs(
                    pad[now_l][0] - pad[num][0]) + abs(pad[now_l][1] - pad[num][1]):
                now_r = num
                answer += 'R'
            elif abs(pad[now_r][0] - pad[num][0]) + abs(pad[now_r][1] - pad[num][1]) > abs(
                    pad[now_l][0] - pad[num][0]) + abs(pad[now_l][1] - pad[num][1]):
                now_l = num
                answer += 'L'
            else:
                if hand == 'right':
                    now_r = num
                    answer += 'R'
                else:
                    now_l = num
                    answer += 'L'

    return answer