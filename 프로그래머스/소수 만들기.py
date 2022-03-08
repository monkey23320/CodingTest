import math as m
from itertools import combinations


def solution(nums):
    answer = 0

    primes = [False] * 50001
    for i in range(2, int(m.sqrt(50000))):
        if primes[i] == False:
            for j in range(i + i, 50001, i):
                primes[j] = True

    for three in list(combinations(nums, 3)):
        if primes[sum(three)] == False:
            answer += 1
    return answer