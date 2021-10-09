import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for val in scoville:
        heapq.heappush(h,val)
    while len(h) > 1 and h[0] < K:
        val1 = heapq.heappop(h)
        val2 = heapq.heappop(h)
        newVal = val1 + 2 * val2
        heapq.heappush(h,newVal)
        answer += 1
        
    if len(h) == 1 and h[0] < K:
        answer = -1
    return answer