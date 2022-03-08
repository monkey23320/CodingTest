s = input()

check_0 = False
check_1 = False

count_0 = 0
count_1 = 0

for i in range(len(s)):
    if s[i] == "0":
        check_1 = True
        if check_0:
            count_0 += 1
            check_0 = False
    if s[i] == "1":
        check_0 = True
        if check_1:
            count_1 += 1
            check_1 = False

if check_0:
    count_0 += 1

if check_1:
    count_1 += 1

print(min(count_0, count_1))