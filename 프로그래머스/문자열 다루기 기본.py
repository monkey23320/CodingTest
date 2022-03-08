def solution(s):
    if len(s) == 4 or len(s) == 6:
        for a in s:
            if '0' <= a <= '9':
                continue
            else:
                return False
        return True
    return False