def solution(s):
    new = s.split(' ')
    result = []
    for word in new:
        new_word = []
        for i in range(len(word)):
            if i %2 == 0:
                new_word.append(word[i].upper())
            else:
                new_word.append(word[i].lower())
        result.append(''.join(new_word))
    return ' '.join(result)