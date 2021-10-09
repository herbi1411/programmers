import heapq
def solution(prices):
    plength = len(prices)
    answer = [0] * plength
    h = []
    for index,price in enumerate(prices):
        while len(h) > 0 and -h[0][0] > price:
            val = heapq.heappop(h)
            answer[val[1]] = index - val[1]
        heapq.heappush(h,(-price,index))
    
    for val, index in h:
        answer[index] = plength - index - 1
    return answer