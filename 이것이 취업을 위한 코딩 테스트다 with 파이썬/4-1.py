n = int(input())
command = list(input().split())
command_move = {'L' : [0, -1], 'R' : [0, 1], 'U' : [-1, 0], 'D' : [1, 0]}


start = [1,1]
for c in command:
    x, y = start[0] + command_move[c][0], start[1] + command_move[c][1]
    if x <= 0 or x > n or y <= 0 or y > n:
        continue
    else:
        start = [x,y]

print(start[0], start[1])
