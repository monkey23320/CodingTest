def solution(enroll, referral, seller, amount):
    answer = []
    parents = {}
    amounts = {}
    for name, parent in zip(enroll, referral):
        if parent == '-':
            parents[name] = 'center'
        else:
            parents[name] = parent

        amounts[name] = 0


    for sell, amount in zip(seller,amount):
        total = amount * 100
        me, parent = sell, parents[sell]
        while True:
            if parent == 'center':
                amounts[me] += (total - (total // 10))
                break
            if (total // 10) < 1:
                amounts[me] += total
                break
            amounts[me] += (total - (total // 10))
            total = total // 10
            me, parent = parent, parents[parent]

    return list(amounts.values())

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])