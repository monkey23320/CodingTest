num = int(input())
base_num = num
cycle = 1
while (1):
    num = ((num % 10) * 10) + (((num % 10) + (num // 10)) % 10)
    if (num == base_num):
        break
    else:
        cycle = cycle + 1
print(cycle)
