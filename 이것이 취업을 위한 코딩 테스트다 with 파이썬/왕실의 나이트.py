pos = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

start = input()
x, y = ord(start[0]) - ord('a'), int(start[1]) - 1

count = 0
for dx, dy in pos:
    if 0 <= x + dx < 8 and 0 <= y + dy < 8:
        count += 1
print(count)
