# from collections import deque
from queue import PriorityQueue

def solution(n, edge):
    answer = 0
    myedge = dict()
    cost = [50001] * (n+1)
    visit = [0] * (n+1)
    queue = PriorityQueue()
    
    for e in edge:
        if e[0] not in myedge:
            myedge[e[0]] = []
        myedge[e[0]].append(e[1])
        
        if e[1] not in myedge:
            myedge[e[1]] = []
        myedge[e[1]].append(e[0])
    
    queue.put((0,1))
    
    while not queue.empty():
        curCost, cur = queue.get()
        if visit[cur] == 1:
            continue

        cost[cur] = curCost
        visit[cur] = 1
        
        for e in myedge[cur]:
            queue.put((curCost+1, e))
    
    del cost[0]
    
    answer = cost.count(max(cost))
    return answer