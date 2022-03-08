def solution(numbers):
    answer = 0
    n = 10 ** len(numbers)

    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    import itertools
    nums = list()
    for i in range(1,len(numbers)+1):
        nums += list(map(int,map(''.join, itertools.permutations(numbers, i))))
    nums = set(nums)

    for k in nums:
        if k in primes:
            answer += 1

    return answer