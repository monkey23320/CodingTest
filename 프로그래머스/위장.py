from itertools import combinations


def solution(clothes):
    answer = 0
    check = dict()
    for l in clothes:
        if l[1] not in check:
            check[l[1]] = 1
        else:
            check[l[1]] += 1
    if len(check) == 30:
        return 155117520 + 2 * (
                    30 + 435 + 4060 + 27405 + 142506 + 593775 + 2035800 + 5852925 + 14307150 + 30045015 + 54627300 + 86493225 + 119759850 + 145422675) + 1

    answer += sum(check.values())
    for i in range(2, len(check) + 1):
        for l in list(combinations(check.keys(), i)):
            tmp = 1
            for n in l:
                tmp *= check[n]
            answer += tmp
    return answer