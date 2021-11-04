def solution(name):
    answer = 0
    changeNum = 0
    switchNum = 0
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
    
    while visitedNum < lenString:
        
        for i in range(len(visit)):
            if visit[cur-i] == 0:
                if cur - i < 0:
                    cur = len(visit) + (cur - i)
                else:
                    cur -= i
                switchNum += i
                break
            if visit[(cur+i) % len(visit)] == 0:
                cur = (cur + i) % len(visit)
                switchNum += i
                break

        visit[cur] = 1
        visitedNum += 1
            
    answer += switchNum     
    return answer