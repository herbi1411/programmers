def solution(enter, leave):
    result = [[0]* len(enter) for _ in range(len(enter))]
    rank = []
    for i in range(1,len(enter)+1):
        rank.append((enter.index(i),leave.index(i)))
    
    for i in range(len(enter)):
        eindex = rank[i][0]
        lindex = rank[i][1]
        for j in range(len(enter)):
            if i == j: continue 
            e2index = rank[j][0]
            l2index = rank[j][1]
            
            if (eindex < e2index and lindex > l2index):
                for k in range(e2index,eindex,-1):
                    result[i][enter[k]-1] = 1
                    result[enter[k]-1][i] = 1
                    
    answer = [sum(result[i]) for i in range(len(result))]
    return answer