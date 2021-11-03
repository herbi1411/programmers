def solution(N, number):
    answer = 0
    # dp = [[] for _ in range(9)]
    dp = [[]] + [[int(str(N) * i)] for i in range(1,9)]
    # dp[1] = [N]
    # print(dp)
    if N == number:
        return 1
    
    # if [number] in dp:
    #     return dp.index([number])
    
    for i in range(2,9):
        # initNum = 0
        # for a in range(i):
        #     initNum = initNum * 10 + 5
        # dp[i].append(initNum)
        # print(initNum)
        for j in range(1,i):
            k = i - j
            for a in dp[j]:
                for b in dp[k]:
                    # print(a,b)
                    dp[i].append(a + b)
                    dp[i].append(a - b)
                    dp[i].append(a * b)
                    if b != 0:
                        dp[i].append(a // b)
        dp[i] = list(set(dp[i]))
        # if 0 in dp[i]:
        #     dp[i].remove(0)
        if number in dp[i]:
            answer = i
            break
        print(dp)
    if answer == 0:
        answer = -1
    # print(dp[7])
    return answer