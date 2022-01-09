def solution(lines):
    answer = 0
    tasks = []
    current = []
    now = 0
    
    for line in lines:
        _,time_string,sec_string = line.split()
        etime = getTimeInteger(time_string)
        stime = getInsertTimeInteger(etime,sec_string)
        tasks.append([stime,etime])
    
    tasks.sort(key=lambda x : x[0])
    
    for stime,etime in tasks:
        now = stime
        deleteTimeout(current,now)
        current.append(etime)
        answer = max(answer,len(current))
        
    # for line in lines:
    #     _,time_string,sec_string = line.split()
    #     time = getTimeInteger(time_string)
    #     now = time
    #     deleteTimeout(current,now)
    #     itime = getInsertTimeInteger(time,sec_string)
    #     current.append(itime)
    #     answer = max(answer,len(current))
    #     print("now: ",now," current: ",current," answer: ",answer)
    return answer


def getTimeInteger(time_string):
    rt = 0
    h,m,sms = time_string.split(":")
    
    s,ms = sms.split(".")
    
    rt += int(ms)
    rt += int(s) * 1000
    rt += int(m) * 1000 * 60
    rt += int(h) * 1000 * 60 * 60
    
    # print(time_string, rt)
    return rt

def deleteTimeout(current,now):
    
    for i in range(len(current)-1,-1,-1):
        if now - current[i] >= 999:
            del current[i]
    
    return current

def getInsertTimeInteger(time,sec_string):
    sec = int(float(sec_string[:-1]) * 1000)
    return time - sec 
        