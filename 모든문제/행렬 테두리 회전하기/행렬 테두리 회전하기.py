def solution(rows, columns, queries):
    answer = []
    matrix = [[columns * i + j + 1 for j in range(columns) ] for i in range(rows) ]
        
    for fx, fy, ex, ey in queries:
        fx, fy, ex, ey = fx-1, fy-1, ex-1, ey-1
        minval = 10001
        
        temp = matrix[fx][fy]
        for ty in range(fy,ey):
            temp2 = matrix[fx][ty+1]
            matrix[fx][ty+1] = temp
            temp = temp2
            minval = min(minval,temp)
            
        for tx in range(fx,ex):
            temp2 = matrix[tx+1][ey]
            matrix[tx+1][ey] = temp
            temp = temp2
            minval = min(minval,temp)
            
        for ty in range(ey,fy,-1):
            temp2 = matrix[ex][ty-1]
            matrix[ex][ty-1] = temp
            temp = temp2
            minval = min(minval,temp)
            
        for tx in range(ex,fx,-1):
            temp2 = matrix[tx-1][fy]
            matrix[tx-1][fy] = temp
            temp = temp2
            minval = min(minval,temp)
            
        answer.append(minval)
    return answer