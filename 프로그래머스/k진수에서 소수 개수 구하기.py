import math
def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def change(n, k):
    change_string = ""
    while n > k:
        change_string = str(n % k) + change_string
        n = n // k
    return str(n) + change_string


def solution(n, k):
    answer = 0
    change_one = ''
    if k != 10:
        change_one = change(n, k)
    else:
        change_one = str(n)
    prime_list = change_one.split('0')
    for num in prime_list:
        if num == '' or num == '1':
            continue
        else:
            if isPrime(int(num)):
                answer += 1
    return answer