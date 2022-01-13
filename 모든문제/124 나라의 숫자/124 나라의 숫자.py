def solution(n):
    answer = ''
    ndict = {0:"1",1:"2",2:"4"}

    num = 0
    while n > 0:
        answer += ndict[((n-1) // (3 ** num)) %3]
        num += 1
        n -= 3 ** num

    answer = answer[::-1]

    return answer