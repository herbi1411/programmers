def solution(n, results):
    answer = 0
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for w, l in results:
        matrix[w][l] = 1
    for k in range(1,n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
    for i in range(1,(n+1)):
        count = 0
        for j in range(1,(n+1)):
            if matrix[i][j] ==1 or matrix[j][i] == 1:
                count += 1
        if count == len(results) - 1:
            answer +=1
    return answer