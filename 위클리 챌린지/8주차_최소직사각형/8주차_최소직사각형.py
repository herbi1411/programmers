def solution(sizes):
    answer = 0
    anstuple = (0,0)
    for x,y in sizes:
        if x >= y:
            anstuple = (max(anstuple[0],x),max(anstuple[1],y))
        else:
            anstuple = (max(anstuple[0],y),max(anstuple[1],x))
    print(anstuple)
    answer = anstuple[0] * anstuple[1]
    return answer