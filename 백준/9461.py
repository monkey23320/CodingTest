import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    test = [0,1,1,1,2,2,3,4,5,7,9]
    target = int(input())
    if target >= len(test):
        for i in range(11, target + 1):
            test.append(test[i-1] + test[i-5])
    print(test[target])
