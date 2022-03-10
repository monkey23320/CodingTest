from itertools import combinations

def solution(relation):
    keys = [x for x in range(len(relation[0]))]
    possible = []
    for i in range(1, len(keys) + 1):
        for key in list(combinations(keys, i)):
            check = []
            for t in relation:
                tmp = []
                for k in list(key):
                    tmp.append(t[k])
                check.append(tuple(tmp))
            if len(list(set(check))) == len(relation):
                final_check = []
                for j in range(1,len(list(key))):
                    final_check = final_check + list(combinations(list(key), j))
                signal = 1
                for p in possible:
                    if p in final_check:
                        signal = 0
                        break
                if signal:
                    possible.append(key)

    return len(possible)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])