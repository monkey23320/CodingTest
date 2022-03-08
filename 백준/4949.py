while True:
    a = input()
    if a == '.': break
    signal = 1
    l = list(a)
    s = list()
    for i in l:
        if i == '(' or i == '[':
            s.append(i)
        elif i == ')':
            if len(s) == 0 or s[-1] == '[':
                signal = 0
                break
            else:
                s.pop()
        elif i == ']':
            if len(s) == 0 or s[-1] == '(':
                signal = 0
                break
            else:
                s.pop()
    if not signal or len(s) > 0:
        print('no')
    else:
        print('yes')
