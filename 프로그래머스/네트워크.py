from collections import deque


def solution(n, computers):
    answer = 0
    visit = [False] * n
    for i in range(n):
        if not visit[i]:
            answer += 1
            visit[i] = True
            q = deque([])
            q.append(i)

            while q:
                index = q.popleft()
                for j in range(n):
                    if index == j:
                        continue
                    if computers[index][j] == 1 and visit[j] == False:
                        visit[j] = True
                        q.append(j)

    return answer