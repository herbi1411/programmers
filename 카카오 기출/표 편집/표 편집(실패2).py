from collections import deque
def solution(n, k, cmd):
    answer = ''
    table = [i for i in range(n)]
    q = deque()
    idx = k
    for c in cmd:
        if c[0] == 'D':
            idx += int(c.split()[1])
        elif c[0] == 'U':
            idx -= int(c.split()[1])
        elif c[0] == 'C':
            q.append((idx,table.pop(idx)))
            if idx == len(table):
                idx -= 1
        elif c[0] == 'Z':
            i, v = q.pop()
            table.insert(i,v)
            if idx >= i:
                idx += 1
    tidx = 0
    for i in range(n):
        if table[tidx] == i:
            answer += 'O'
            tidx += 1
        else:
            answer += 'X'            
    return answer