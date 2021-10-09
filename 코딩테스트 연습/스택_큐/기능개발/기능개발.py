def solution(progresses, speeds):
    answer = []
    days=  []
    
    for p,s in zip(progresses,speeds):
        temp = (100-p) % s
        if temp == 0:
            days.append((100-p) // s)
        else:
            days.append((100-p) // s + 1)
            
    daysIndex = 0
    while(daysIndex < len(days)):
        daysIndex2 = daysIndex+1
        while True:
            if daysIndex2 < len(days) and days[daysIndex] >= days[daysIndex2]:
                daysIndex2 += 1
            else:
                break
        answer.append(daysIndex2 - daysIndex)
        daysIndex = daysIndex2
    print(days)
    print(answer)
    return answer