def solution(N, stages):
    answer = []
    sdict = dict()
    sorted_list = []
    
    for i in range(N):
        sdict[i] = [0] * 2
        
    for val in stages:
        for j in range(min(val, N)):
            sdict[j][1] += 1
        if (val - 1 < N):
            sdict[val - 1][0] += 1

    for key in sdict:
        sdict[key] = sdict[key][0] / sdict[key][1]
    
    sorted_list = sorted(list(sdict.items()), key=lambda x: x[1], reverse = True)
    answer = [a[0] + 1 for a in sorted_list]
    return answer