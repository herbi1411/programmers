def solution(N, number):
    
    visit = [-1] * getNum(N,8)
    
    stage = [N]
    for i in range(1,8):
        prev = stage
        stage = []
        stage.append(prev[0]+pow(10,i) * N)
        for i in range(1,len(prev)):
            val = prev[i]
            
            temp = val + N
            if temp >=0 and  temp not in stage:
                temp
        print(stage)
    answer = 0
    return answer


def getNum(N, number):
    rt = 0
    mul = 1
    for i in range(number):
        rt += N * mul
        mul *=10
    return rt