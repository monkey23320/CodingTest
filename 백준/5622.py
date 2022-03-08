string = input()
sum1 = 0
for i in string:
    if(i == 'A' or i == 'B' or i == 'C'):
        sum1 += 2
    elif(i == 'D' or i == 'E' or i == 'F'):
        sum1 += 3
    elif(i == 'G' or i == 'H' or i == 'I'):
        sum1 += 4
    elif(i == 'J' or i == 'K' or i == 'L'):
        sum1 += 5
    elif(i == 'M' or i == 'N' or i == 'O'):
        sum1 += 6
    elif(i == 'P' or i == 'Q' or i == 'R' or i == 'S'):
        sum1 += 7
    elif(i == 'T' or i == 'U' or i == 'V'):
        sum1 += 8
    else:
        sum1 += 9
print(sum1 + len(string))
