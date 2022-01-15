from collections import deque
def solution(s):
    answer = -1
    dq = deque()
    for a in s:
        if len(dq) == 0 or dq[-1] != a :
            dq.append(a)
        else:
            dq.pop()
    
    answer = int((len(dq) == 0))

    return answer