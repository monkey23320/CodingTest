def solution(rows, columns, queries):
    answer = []
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    numbers = []
    for i in range(rows):
        numbers.append(list(range(columns * i + 1, columns * (i + 1) + 1)))

    for x1, y1, x2, y2 in queries:
        start_x, start_y = x1 - 1, y1 - 1
        next_x, next_y = x1 - 1, y1
        tmp = numbers[start_x][start_y]
        d = 0
        min_num = tmp
        flag = 0
        while start_x != x1 - 1 or start_y != y1 - 1 or flag != 1:
            flag = 1
            tmp, numbers[next_x][next_y] = numbers[next_x][next_y], tmp
            if min_num > tmp:
                min_num = tmp

            start_x, start_y = next_x, next_y

            if x1 - 1 <= next_x + dirs[d][0] <= x2 - 1 and y1 - 1 <= next_y + dirs[d][1] <= y2 - 1:
                next_x, next_y = next_x + dirs[d][0], next_y + dirs[d][1]
            else:
                d += 1
                if d == 4:
                    d = 0
                next_x, next_y = next_x + dirs[d][0], next_y + dirs[d][1]
        answer.append(min_num)

    return answer