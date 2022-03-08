def solution(s):
    result = 1000
    for i in range(1, len(s) // 2 + 2):
        c = ""
        prev = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if prev == s[j:j + i]:
                count += 1
            else:
                c += str(count) + prev if count >= 2 else prev
                prev = s[j:j + i]
                count = 1
        c += str(count) + prev if count >= 2 else prev
        result = min(result, len(c))

    return result