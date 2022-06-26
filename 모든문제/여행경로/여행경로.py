from collections import deque

def DFS(cur, rdict, visit, route, routes, depth, tickets):
    check = True
    for v in visit.values():
        if v == 0:
            check = False
            break
    if check and depth == len(tickets):
        routes.append(list(route))
        return
    for i, val in enumerate(rdict[cur]):
        city = val[0]
        if not rdict[cur][i][1]:
            visit[city] += 1
            rdict[cur][i][1] = True
            route.append(city)
            DFS(city, rdict, visit, route, routes, depth + 1, tickets)
            rdict[cur][i][1] = False
            route.pop()
            visit[city] -= 1

def solution(tickets):
    answer = []
    routes = []
    route = deque()
    rdict = {}
    visit = {}
    for depart, arrival in tickets:
        if depart not in rdict:
            rdict[depart] = []
        if arrival not in rdict:
            rdict[arrival] = []
        rdict[depart].append([arrival, False])
    for city in rdict.keys():
        visit[city] = 0
    visit["ICN"] += 1
    route.append("ICN")
    DFS("ICN", rdict, visit, route, routes, 0, tickets)
    routes.sort()
    answer = routes[0]
    return answer