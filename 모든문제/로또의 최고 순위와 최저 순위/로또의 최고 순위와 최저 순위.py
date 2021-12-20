def solution(lottos, win_nums):
    answer = []
    zeros = getZeroNums(lottos)
    correct = getCorrectNums(lottos,win_nums)
    
    answer = [min(6,6-correct-zeros+1),min(6,6-correct+1)]

    return answer

def getCorrectNums(lottos,win_nums):
    rt = 0
    for i in lottos:
        if i in win_nums:
            rt += 1
    return rt
def getZeroNums(arr):
    rt = 0
    for i in arr:
        if i == 0:
            rt+=1
    return rt