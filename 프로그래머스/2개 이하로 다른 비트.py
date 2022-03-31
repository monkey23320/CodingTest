def solution(numbers):
    answer = []
    for n in numbers:
        n = int(n)
        binary = format(n, 'b')
        if n == 0:
            answer.append(1)
        elif n ^ int('1' * len(binary),2) == 0:
            answer.append(int('10'+format(n, 'b')[1:], 2))
        else:
            binary = list(binary)
            check = len(binary)
            for i in range(len(binary) - 1, 0, -1):
                if binary[i] == '0':
                    binary[i] = '1'

                    break
                else:
                    check = i
            if len(binary) - check != 0:
                binary[check] = '0'


            answer.append(int(''.join(binary),2))

    return answer


solution([2, 7])
