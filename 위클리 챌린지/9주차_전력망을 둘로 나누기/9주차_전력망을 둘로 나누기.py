def solution(n, wires):
    answer = -1
    results = []
    
    for (i,wire) in enumerate(wires):
        tempwires = wires[:]
        del tempwires[i]
        visit = [0] * (n+1)
        dfs(1,tempwires,visit)
        
        temp = sum(visit)
        if temp > n // 2:
            temp = n - temp
        results.append(n -2 * temp)
    answer = min(results)
    
    return answer



def dfs(location,wires,visit):
    if visit[location] == 1:
        return
    else:
        visit[location] = 1
        for wire in wires:
            if wire[0] == location:
                dfs(wire[1],wires,visit)
            elif wire[1] == location:
                dfs(wire[0],wires,visit)