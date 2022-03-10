def solution(numbers):
    answer = ""
    numbers = [str(a) * 3 for a in numbers]
    numbers.sort(reverse = True)
    answer = ''.join([a[:len(a)//3] for a in numbers])
    if int(answer) == 0:
        return '0'
    else:
        return answer