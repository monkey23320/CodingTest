n = int(input())

students = []
for _ in range(n):
    inputs = input().split()
    students.append((inputs[0], int(inputs[1])))

students.sort(key = lambda x : x[1])

for data in students:
    print(data[0], end = ' ')

