def solution(numbers, target):
    answer = 0
    
    now = []
    plus = []
    minus = []
    
    now.append(numbers[0])
    now.append(-numbers[0])
    
    for i in range(1,len(numbers)):
        plus = [a+numbers[i] for a in now]
        minus = [a-numbers[i] for a in now]
        
        now = plus + minus
    
    for v in now:
        if v == target:
            answer += 1
    return answer