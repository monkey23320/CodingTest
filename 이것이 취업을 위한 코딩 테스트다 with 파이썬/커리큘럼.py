from collections import deque

n = int(input())
sub = [0] * (n+1)
time = [0] * (n+1)
first = [[] for _ in range(n+1)]
end_time = [0] * (n+1)
for i in range(n):
    info = list(map(int, input().split()))
    end_time[i + 1] = info[0]
    time[i+1], info = info[0], info[1:]

    for k in info:
        if k == -1:
            break
        first[k].append(i+1)
        sub[i+1] += 1



q = deque([])
for i in range(1, n+1):
    if sub[i] == 0:
        q.append(i)

while q:
    subject = q.popleft()
    for i in first[subject]:
        end_time[i] = max(end_time[i], end_time[subject] + time[i])
        sub[i] -= 1
        if sub[i] == 0:
            q.append(i)

for i in range(1,n+1):
    print(end_time[i])
