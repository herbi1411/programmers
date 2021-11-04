def solution(name):
    answer = 0
    changeNum = 0
    switchNum = [len(name)]
    lenString = len(name)
    visitedNum = 0
    cur = 0
    
    visit = [0] * len(name)
    for i, ch in enumerate(name):
        if ch == "A":
            visit[i] = 1
            visitedNum += 1
        temp = ord(ch) - ord("A")
        temp = min(26-temp,temp)
        # print(ch,temp)
        changeNum += temp
    answer += changeNum
    
    dfs(0,visitedNum,0,visit,switchNum) 
    
    # print("switchNum[0]",switchNum[0])
    answer += switchNum[0]    
    return answer


def dfs(cur,num,swnum,visit,result):
    # print(cur,num,swnum,visit,result)
    if num == len(visit):
        result[0] = min(result[0],swnum)
        # print("swnum",swnum,"result",result)
        return
    
    for i in range(len(visit)):
        if visit[(cur+i) % len(visit)] == 0:
            visit[(cur+i)%len(visit)] = 1
            dfs((cur+i) % len(visit),num+1,swnum+i,visit,result)
            visit[(cur+i)%len(visit)] = 0
            break
    for i in range(len(visit)):
        if visit[cur-i] == 0:
            visit[cur-i] = 1
            if cur-i < 0:
                ncur = len(visit) + (cur-i)
            else:
                ncur = cur - i 
            dfs(ncur,num+1,swnum+i,visit,result)
            visit[cur-i] = 0
            break