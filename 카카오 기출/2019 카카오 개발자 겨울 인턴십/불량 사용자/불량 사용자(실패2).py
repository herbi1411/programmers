from collections import Counter

def dfs(stage,temp,visit,user_id,banned_id,result):
    if stage == len(banned_id):
        temp.sort()
        print(temp)
        if temp not in result:
            result.append(temp)
    
    for k,uid in enumerate(user_id):
        if len(uid) != len(banned_id) or visit[k] == 1:
            continue
        else:
            flag = True
            for i in len(uid):
                if banned_id[stage][i] == "*" or banned_id[stage][i] == uid[i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                visit[k] = 1
                temp.append(uid)
                dfs(stage+1,temp,visit,user_id,banned_id,result)
                temp.remove(uid)
                visit[k] = 0
                
def solution(user_id, banned_id):
    answer = 0
    result = []
    visit = [0] * len(user_id)
    
    dfs(0,[],visit,user_id,banned_id,result)
    print(result)
    answer = len(result)
    return answer