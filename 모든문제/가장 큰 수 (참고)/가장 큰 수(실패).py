from itertools import permutations
def solution(numbers):
    answer = ""
    numbers = [str(a) for a in numbers]
    cb = list(permutations(numbers,len(numbers)))
    cb = [''.join(a) for a in cb]
    answer = max([int(a) for a in cb])
    answer = str(answer)
    return answer