def solution(sizes):
    answer = 0
    long = []
    short = []
    for a, b in sizes:
        if a > b:
            long.append(a)
            short.append(b)
        else:
            long.append(b)
            short.append(a)

    return max(long) * max(short)