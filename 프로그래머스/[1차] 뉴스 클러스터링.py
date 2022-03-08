def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_l = {}
    str2_l = {}

    for i in range(len(str1) - 1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i + 1] <= 'z':
            if str1[i:i + 2] not in str1_l:
                str1_l[str1[i:i + 2]] = 1
            else:
                str1_l[str1[i:i + 2]] += 1

    for i in range(len(str2) - 1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i + 1] <= 'z':
            if str2[i:i + 2] not in str2_l:
                str2_l[str2[i:i + 2]] = 1
            else:
                str2_l[str2[i:i + 2]] += 1
    print(str1_l)
    print(str2_l)
    duple = 0
    if len(str1_l) == 0 and len(str2_l) == 0:
        answer = 1
    else:
        for key, value in str1_l.items():
            if key in str2_l:
                duple += min(value, str2_l[key])
        answer = duple / (sum(str1_l.values()) + sum(str2_l.values()) - duple)
    return int(answer * 65536)