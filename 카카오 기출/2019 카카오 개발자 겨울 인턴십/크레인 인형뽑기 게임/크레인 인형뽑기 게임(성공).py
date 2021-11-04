from collections import deque
def solution(board, moves):
    answer = 0
    top = [len(board)] * len(board[0]) 
    q = deque()
    for i,row in enumerate(board):
        # print(row)
        for j,val in enumerate(row):
            if val != 0 and top[j] == len(board):
                top[j] = i
    # print(top)
    for command in moves:
        command -= 1
        if top[command] >= len(board):
            continue
        target = board[top[command]][command]
        top[command] += 1
        if len(q) >0 and q[-1] == target:
            q.pop()
            answer += 2
        else:
            q.append(target)
    return answer