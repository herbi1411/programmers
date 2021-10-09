def solution(jobs):
    answer = 0
    curtime = 0
    eindex = 0
    curjob = []
    jobslength = len(jobs)
    jobs.sort(key= lambda x: (x[0],x[1]))
    
    while len(jobs) > 0:
        eindex = 0
        while eindex <len(jobs) and jobs[eindex][0] <=curtime:
            eindex += 1
        if eindex == 0:
            curtime += 1
            continue
        curjob = min(jobs[0:eindex],key=lambda x: x[1])
        curtime += curjob[1]
        answer += curtime - curjob[0]
        jobs.remove(curjob)
    
    answer //= jobslength
    return answer