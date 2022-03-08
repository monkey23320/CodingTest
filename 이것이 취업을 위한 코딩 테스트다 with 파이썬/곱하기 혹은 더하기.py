numbers = list(map(int, list(input())))

initial = numbers[0]

for num in numbers[1:]:
    # if initial <= 1 or num <= 1:
    if initial == 0 or initial == 1 or num == 0 or num == 1:
        initial += num
    else:
        initial *= num

print(initial)