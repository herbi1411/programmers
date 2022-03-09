def find_end_pair(p, now):
    temp = 0
    rt = now
    for (i, val) in enumerate(p[now:]):
        if val == '(':
            temp += 1
        elif val == ')':
            temp -= 1
        if i != 0 and temp == 0:
            rt = i + now
            break
    return rt

def is_correct_str(p, st, end):
    temp = 0
    for i in range(st,end+1):
        if p[i] == '(':
            temp += 1
        elif p[i] == ')':
            temp -= 1
        if temp < 0:
            break
    return (temp == 0)

def func(answer, p, u, v, length):
    if is_correct_str(p, u, v):
        answer.append(p[u:v+1])
        if v + 1 < length:
            func(answer, p, v+1, find_end_pair(p,v+1), length)
    else:
        temp = []
        temp.append('(')
        if v + 1 < length:
            func(temp, p, v+1, find_end_pair(p,v+1), length)
        temp.append(')')
        for val in p[u+1:v]:
            if val == '(':
                temp.append(')')
            elif val == ')':
                temp.append('(')
        answer += temp
    
def solution(p):
    answer = []
    if len(p) == 0:
        return ''
    func(answer, p, 0, find_end_pair(p, 0), len(p))
    return ''.join(answer)