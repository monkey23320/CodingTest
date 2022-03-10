from itertools import combinations
def solution(orders, course):
    answer = []
    menu = list(combinations(orders, 2))
    menu_count = {}
    max_count = {}
    for c in course:
        max_count[str(c)] = 0

    for a, b in menu:
        set_a, set_b = set(list(a)), set(list(b))
        final_set = sorted(list(set_a & set_b))

        for i in range(1,len(final_set)+1):
            if i in course:
                for m in list(combinations(final_set, i)):
                    course_name = ''.join(list(m))
                    if course_name in menu_count:
                        menu_count[course_name] += 1
                    else:
                        menu_count[course_name] = 1

    menu_count = sorted(menu_count.items(), key = lambda x : x[1], reverse=True)

    for m, cnt in menu_count:
        if max_count[str(len(m))] == 0:
            max_count[str(len(m))] = cnt
            answer.append(m)
            continue

        if max_count[str(len(m))] == cnt:
            answer.append(m)

    answer.sort()
    return answer
