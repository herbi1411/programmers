def solution(clothes):
    answer = 1
    cdict = dict()
    for cloth in clothes:
        cname = cloth[0]
        ccategory = cloth[1]
        if ccategory in cdict:
            cdict[ccategory] += 1
        else:
            cdict[ccategory] = 1
    
    dicvalues = cdict.values()
    for a in dicvalues:
        answer *= (a+1)
    answer -= 1
    return answer