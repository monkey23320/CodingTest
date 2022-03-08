import math
def solution(fees, records):
    answer = []
    parking_check = {}
    time = {}
    for record in records:
        clock, car_id, stage = record.split(' ')
        clock = int(clock[:2]) * 60 + int(clock[3:])
        if stage == 'IN':
            parking_check[car_id] = clock
            if car_id not in time.keys():
                time[car_id] = 0
        else:
            time[car_id] += clock - parking_check[car_id]
            parking_check[car_id] = -1

    for car_id, clock in parking_check.items():
        if clock != -1:
            time[car_id] += 1439 - clock

    sorted_time = sorted(time.items(), key = lambda x : x[0])
    for t in sorted_time:
        total = 0
        if t[1] <= fees[0]:
            total = fees[1]
        else:
            total = fees[1] + int(math.ceil((t[1] - fees[0]) / fees[2])) * fees[3]
        answer.append(total)
    return answer