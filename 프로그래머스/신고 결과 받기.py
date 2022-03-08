def solution(id_list, report, k):
    mail = {}
    count = {}
    for id in id_list:
        mail[id] = []
        count[id] = 0

    for re in report:
        attacker, defender = re.split(' ')

        if not defender in mail[attacker]:
            mail[attacker].append(defender)
            count[defender] += 1

    answer = []
    for id in id_list:
        num = 0
        for id_check in mail[id]:
            if count[id_check] >= k:
                num += 1
        answer.append(num)
    return answer