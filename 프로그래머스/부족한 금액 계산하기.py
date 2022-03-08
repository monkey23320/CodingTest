def solution(price, money, count):
    total = count * (count + 1) / 2
    if money >= total * price:
        return 0
    else:
        return total * price - money