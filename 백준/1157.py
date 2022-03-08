string = input().upper()
set1= set()
for i in string:
    set1.add(i)
tf = 0
max_num = 0
max_index = 0
set1 = list(set1)
for i in range(len(set1)):
    if(max_num < string.count(set1[i])):
        max_num = string.count(set1[i])
        max_index = i
        tf = 1
    elif(max_num == string.count(set1[i])):
        tf = -1
if(tf == 1):
    print(set1[max_index])
else:
    print('?')
