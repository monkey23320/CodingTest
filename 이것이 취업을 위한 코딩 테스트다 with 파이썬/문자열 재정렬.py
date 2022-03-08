s = list(input())
s.sort()

index = 0

for i, x in enumerate(s):
   if x >= 'A':
        index = i
        break

print(''.join(s[index:]) + str(sum(map(int, s[:index]))))