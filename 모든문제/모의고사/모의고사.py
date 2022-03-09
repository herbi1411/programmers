def solution(answers):
    answer = []
    temp = [0] * 3
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    for (i,val) in enumerate(answers):
        if val == a1[i % len(a1)]:
            temp[0] += 1
        if val == a2[i % len(a2)]:
            temp[1] += 1
        if val == a3[i % len(a3)]:
            temp[2] += 1
    
    for i in range(3):
        if temp[i] == max(temp):
            answer.append(i+1)
            
    return answer