
def solution(numbers):
    nums = [((str(x) * 4)[:4], len(str(x))) for x in numbers]
    nums.sort(reverse=True)
    answer = ''
    for x, l in nums:
        answer += x[:l]
    if int(answer) == 0:
        return '0'
    return answer

print(solution([3,30,34,5,9]))