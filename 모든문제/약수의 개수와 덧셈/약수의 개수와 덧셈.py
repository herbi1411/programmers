import math

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num % math.sqrt(num) == 0:
            answer -= num
        else:
            answer += num
    return answer