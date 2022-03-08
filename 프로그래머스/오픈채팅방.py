def solution(record):
    answer = []
    id_list = {}
    for message in record:
        command = list(message.split(' '))
        if command[0] == 'Enter' or  command[0] == 'Change':
            id_list[command[1]] = command[2]
    for message in record:
        command = list(message.split(' '))
        if command[0] == 'Enter':
            answer.append(id_list[command[1]] + "님이 들어왔습니다.")
        elif command[0] == 'Leave':
            answer.append(id_list[command[1]] + "님이 나갔습니다.")
    return answer