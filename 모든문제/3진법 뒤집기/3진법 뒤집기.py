def solution(n):
    answer = 0
    str3 = ''
    
    while n > 0:
        str3 += str(n % 3)
        n //= 3
    for a in str3:
        answer = answer * 3 + int(a)
    return answer