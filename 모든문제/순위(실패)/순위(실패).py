def recur_win(wl_arr, target):
    for nt in wl_arr[target][0]:
        wl_arr[nt][1] |= wl_arr[target][1]
        recur_win(wl_arr, nt)

def recur_lose(wl_arr, target):
    for nt in wl_arr[target][1]:
        wl_arr[nt][0] |=wl_arr[target][0]
        recur_win(wl_arr, nt)

def solution(n, results):
    answer = 0
    wl_arr = [[set(),set()] for _ in range(n + 1)]
    for w,l in results:
        wl_arr[w][1] |= wl_arr[l][1]
        wl_arr[w][1].add(l)
        wl_arr[l][0] |= wl_arr[w][0]
        wl_arr[l][0].add(w)
        recur_win(wl_arr,w)
        recur_lose(wl_arr,l)
        
    for ws, ls in wl_arr:
        if len(ws) + len(ls) == len(results) - 1:
            answer += 1
    return answer