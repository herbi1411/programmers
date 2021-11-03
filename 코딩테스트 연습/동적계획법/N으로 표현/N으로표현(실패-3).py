def solution(N, number):
    answer = 0
    dp = [[0] for _ in range(9)]
    dp[1] = [N]
    if N == number:
        return 1
    
    for i in range(2,9):
        initNum = 0
        for a in range(i):
            initNum = initNum * 10 + 5
        dp[i].append(initNum)
        for j in range(1,i):
            k = i - j
            for a in dp[j]:
                for b in dp[k]:
                    # print(a,b)
                    dp[i].append(a + b)
                    dp[i].append(a - b)
                    dp[i].append(a * b)
                    dp[i].append(a // b)
        dp[i] = list(set(dp[i]))
        if 0 in dp[i]:
            dp[i].remove(0)
        if number in dp[i]:
            answer = i
            break
        if answer == 0:
            answer = -1
    return answer