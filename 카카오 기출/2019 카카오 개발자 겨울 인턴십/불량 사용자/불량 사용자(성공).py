def dfs(stage,visit,temp,user_id,banned_list,rlist)
    
    if stage == len(banned_list)
        temp.sort()
        # print(temp,temp, type(temp))
        flag = True
        for r in rlist
            if len(r) != len(temp)
                continue
            flag2 = True
            for i,t in enumerate(temp)
                if r[i] == t
                    continue
                else
                    flag2 = False
                    break
            if flag2 == True
                flag = False
                break
        if flag
            rlist.append(temp[])
            # print(rlist)
        return
    
    for val in banned_list[stage]
        if visit[val] == 1
            continue
        else
            visit[val] = 1
            temp.append(user_id[val])
            dfs(stage+1,visit,temp,user_id,banned_list,rlist)
            temp.remove(user_id[val])
            visit[val] = 0
            
def solution(user_id, banned_id)
    answer = 0
    rlist = []
    visit = [0]  len(user_id)
    banned_list = [[] for _ in range(len(banned_id))]
    
    for i,bid in enumerate(banned_id)
        for j,uid in enumerate(user_id)
            if len(bid) != len(uid)
                continue
                
            flag = True
            for k,c in enumerate(uid)
                if bid[k] ==  or bid[k] == c
                    continue
                else
                    flag = False
                    break
            if flag
                banned_list[i].append(j)
    # print(banned_list)
    dfs(0,visit,[],user_id,banned_list,rlist)
    answer = len(rlist)
    # print(rlist)
    return answer