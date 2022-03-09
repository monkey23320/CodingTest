from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    check = [[False] * m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        check[x][y] = True
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if not check[nx][ny] and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))