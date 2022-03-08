string = input()
num = 0
i = 0
while i < len(string):
    if i < len(string) - 2:
        if string[i:i+3] == 'dz=':
            num += 1
            i+= 3
            continue
    if i < len(string) - 1:
        if string[i:i+2] == 'c=' or string[i:i+2] == 'c-' or string[i:i+2] == 's=' or string[i:i+2] == 'z=' or string[i:i+2] == 'd-' or string[i:i+2] == 'lj' or string[i:i+2] == 'nj':
            num += 1
            i += 2
            continue
    num+=1
    i+=1
print(num)