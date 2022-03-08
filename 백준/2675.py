test = int(input())
for i in range(test):
    rep, word = input().split()
    for j in range(len(word)):
        if(j==len(word)-1):
            print(word[j]*int(rep))
        else:
            print(word[j]*int(rep), end='')