#베낌 : https://westmino.tistory.com/20
def solution(n, results):
    answer = 0
    matrix = [[0] * n for _ in range(n)]
    for w, l in results:
        matrix[w-1][l-1] = 1
        matrix[l-1][w-1] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if i == j or matrix[i][j] in [-1,1]:
                #     continue
                if matrix[i][k] == matrix[k][j] == 1:
                    matrix[i][j] = 1
                    matrix[j][i] = -1
    for row in matrix:
        if row.count(0) == 1:
            answer +=1
    return answer

#ver 2
def solution(n, results):
    answer = 0
    matrix = [[0] * n for _ in range(n)]
    for w, l in results:
        matrix[w-1][l-1] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] == 1 or matrix[j][i] == 1:
                count += 1
        if count == n - 1:
            answer +=1
    return answer

    