def solution(k, dungeons):
    answer = -1
    maxval = [0]
    visit = [0] * len(dungeons)
    dfs(dungeons,k,visit,maxval,0)
    answer = maxval[0]
    return answer


def dfs(dungeons,pirodo,visit,maxval,step):
    
    maxval[0] = max(maxval[0],step)
    # print(step,visit,pirodo)
    if step == len(dungeons):
        return 
    for i,dungeon in enumerate(dungeons):
        if visit[i] == 1:
            continue
        else:
            if pirodo >= dungeon[0]:
                pirodo -= dungeon[1]
                visit[i] = 1
                dfs(dungeons,pirodo,visit,maxval,step+1)
                visit[i] = 0
                pirodo += dungeon[1]