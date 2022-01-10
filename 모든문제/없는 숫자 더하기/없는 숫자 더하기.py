def solution(numbers):
    answer = -1
    answer = 0
    
    numarr = [0 for _ in range(10)]
    
    for num in numbers:
        numarr[num] = 1
    
    for i,val in enumerate(numarr):
        if val == 0:
            answer += i
    
    return answer