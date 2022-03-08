def solution(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        semi = []
        for c,d in zip(a,b):
            semi.append(c+d)
        result.append(semi)
    return result