def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif 'A' <= c <= 'Z':
            if ord(c) + n > ord('Z'):
                answer += chr(ord(c) + n - 26)
            else:
                answer += chr(ord(c) + n)
        else:
            if ord(c) + n > ord('z'):
                answer += chr(ord(c) + n - 26)
            else:
                answer += chr(ord(c) + n)

    return answer