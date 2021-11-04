from collections import deque
def solution(board, moves):
    answer = 0
    top = [0] * len(board)
    for (k,row) in enumerate(board):
        # print(row)
        for (i,val)in enumerate(row):
            if val != 0 and top[i] == 0:
                top[i] = k
    # print(top)
                
            
    
    q = deque()
    for val in moves:
        val -= 1
        # print(top[val])
        if top[val] >= len(board):
            continue
        target = board[top[val]][val]
        if len(q) > 0 and q[-1] == target:
            q.pop()
            answer+=2
        else:
            q.append(target)
        top[val] += 1 
        # print(val,target, top, q)
    return answer