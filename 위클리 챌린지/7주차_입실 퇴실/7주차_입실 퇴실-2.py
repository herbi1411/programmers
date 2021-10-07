def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    s_enter = len(enter)
    s_leave = len(leave)
    c_enter = 0
    c_leave = 0
    
    while(c_leave < s_leave):
        if leave[c_leave] in room:
            answer[leave[c_leave]-1] += len(room) - 2
            for a in room:
                answer[a-1] += 1
            room.remove(leave[c_leave])
            c_leave += 1
        else:
            room.append(enter[c_enter])
            c_enter += 1
                
    return answer