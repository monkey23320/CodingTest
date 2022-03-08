import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for k in scoville:
        heapq.heappush(q, k)

    while len(q) >= 2:
        k1 = heapq.heappop(q)
        if k1 >= K:
            heapq.heappush(q, k1)
            break
        k2 = heapq.heappop(q)
        heapq.heappush(q, k1 + (k2 * 2))
        answer += 1

    if heapq.heappop(q) < K:
        return -1
    else:
        return answer