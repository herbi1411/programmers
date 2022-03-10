from functools import cmp_to_key

def compare(a,b):
    max_len = max(len(a),len(b))
    for i in range(max_len):
        if i >= len(a):
            v1 = a[-1]
        else:
            v1 = a[i]
        if i >= len(b):
            v2 = b[-1]
        else:
            v2 = b[i] 
        if v1 > v2:
            return -1
        elif v1 < v2:
            return 1
    return 1

def solution(numbers):
    answer = ""
    numbers = [str(a) for a in numbers]
    numbers.sort(key=cmp_to_key(compare))
    answer = ''.join(numbers)
    return answer