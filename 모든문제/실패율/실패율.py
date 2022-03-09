from collections import Counter
def solution(N, stages):
    answer = []
    sdict = {}
    temp = 0
    for i in range(N):
        sdict[i] = 0
    ct = sorted(list(dict(Counter(stages)).items()), key= lambda x: x[0], reverse= True)
    for stage, num in ct:
        if stage <= N:
            sdict[stage - 1] = num / (num + temp)
        temp += num
    answer = [a[0] + 1 for a in sorted(list(sdict.items()), key = lambda x: x[1], reverse= True)]
    return answer