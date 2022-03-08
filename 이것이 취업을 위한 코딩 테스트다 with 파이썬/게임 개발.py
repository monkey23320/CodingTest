go = [(0, -1), (1, 0), (0, 1), (-1, 0)]

n, m = map(int, input().split())
y, x, pos = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

maps[y][x] = 2
count = 1
while True:
    check = True
    for _ in range(4):
        new_x, new_y = x + go[pos][0], y + go[pos][1]
        if 0 <= new_x < m and 0 <= new_y < n and maps[new_y][new_x] == 0:
            maps[new_y][new_x] = 2
            count += 1
            x, y = new_x, new_y
            check = False
            break
        else:
            pos -= 1
            if pos < 0:
                pos = 3
    if check:
        tmp_pos = pos - 2
        if tmp_pos < 0:
            tmp_pos += 4
        back_x, back_y = x + go[tmp_pos][0], y + go[tmp_pos][1]
        if 0 > back_x or back_x >= m or back_y < 0 or back_y > n or maps[back_y][back_x] == 1:
            break
        else:
            x, y = back_x, back_y
print(count)
