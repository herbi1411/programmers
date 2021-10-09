import math
def solution(brown, yellow):
    answer = []
    divisors = getDivisor(yellow)
    
    for num1 in divisors:
        num2 = yellow // num1
        tbrown = (num1 + num2) * 2 + 4
        if tbrown == brown:
            answer = [num2+2,num1+2]
            break
    return answer

def getDivisor(num):
    rlist = []
    divisor = 1
    maxnum = math.sqrt(num)
    
    while divisor <= maxnum:
        if num % divisor == 0:
            rlist.append(divisor)
        divisor +=1
        
    return rlist
    