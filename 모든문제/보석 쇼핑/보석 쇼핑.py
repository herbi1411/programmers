def solution(gems):
    answer = []
    gdict = {}
    glen = len(set(gems))
    st = 0
    for i,gem in enumerate(gems):
        if gem not in gdict:
            gdict[gem] = 0
        gdict[gem] += 1
        for j in range(st, i):
            if gdict[gems[j]] > 1:
                gdict[gems[j]] -= 1
                st += 1
            else:
                break
        if len(gdict) == glen:
            answer.append([st,i])
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return [answer[0][0] + 1, answer[0][1] + 1]