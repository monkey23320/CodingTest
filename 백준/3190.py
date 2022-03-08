from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

apple = int(input())

for _ in range(apple):
    col, row = map(int, input().split())
    board[col][row] = 1

dirs = [0] * 10001
direct = int(input())
for _ in range(direct):
    t, cir = input().split()
    dirs[int(t)] = cir

snake = deque([[1, 1]])
board[1][1] = 2
dir = 0
answer = 0
dir_col = [1, 0, -1, 0]
dir_row = [0, 1, 0, -1]


def change_dir(now, com):
    if com == 'L':
        now -= 1
    else:
        now += 1

    if now < 0:
        return 3
    elif now > 3:
        return 0
    else:
        return now


while True:
    answer += 1
    head = snake[-1].copy()
    head[0], head[1] = head[0] + dir_row[dir], head[1] + dir_col[dir]
    # 게임 끝?
    if head[0] < 1 or head[0] > n or head[1] > n or head[1] < 1 or board[head[0]][head[1]] == 2:
        break

    if board[head[0]][head[1]] == 0:
        tail = snake.popleft()
        board[tail[0]][tail[1]] = 0

    board[head[0]][head[1]] = 2
    snake.append(head)

    if dirs[answer] != 0:
        dir = change_dir(dir, dirs[answer])

    # for i in range(1,n+1):
    #     print(board[i][1:])
    # print('\n')

print(answer)
