import heapq
def solution(board):
    answer = 0
    N = len(board)
    cost = [[[987654321] * 4 for _ in range(N)] for __ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    heapq.heappush(q,(0,0,0,-1))
    while len(q) > 0:
        curcost, curx, cury, direction = heapq.heappop(q)
        i = 0
        for tx, ty in zip(dx,dy):
            nx = curx + tx
            ny = cury + ty
            ncost = 0
            if direction == -1 or direction == i:
                ncost = curcost + 100
            else:
                ncost = curcost + 100 + 500
            if 0<=nx<N and 0<=ny<N and ncost < cost[nx][ny][i] and board[nx][ny] != 1:
                heapq.heappush(q,(ncost, nx, ny, i))
                cost[nx][ny][i] = ncost
            i += 1
    answer = min(cost[N-1][N-1])
    return answer