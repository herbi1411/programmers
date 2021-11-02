def solution(n, lost, reserve):
    answer = 0
    
    # for v in reserve:
    #     if v in lost:
    #         reserve.remove(v)
    #         lost.remove(v)
    
    _reserve = [a for a in reserve if a not in lost]
    _lost = [b for b in lost if b not in reserve]
    
    reserve = _reserve
    lost = _lost

    reserve.sort()
    lost.sort()
    
    for a in lost:
        for v in reserve:
            if a -1 == v or a + 1 == v:
                answer +=1
                reserve.remove(v)
                break

    return n - len(lost) + answer
#     for v in reserve:
#         if v-1 in lost:
#             lost.remove(v-1)
#         elif v+1 in lost:
#             lost.remove(v+1)
            
#     return n - len(lost)