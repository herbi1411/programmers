def solution(N, number):
    answer = 0
    stage = 2
    temp = []
    numarr = [N]
    while stage <= 8:
        temp = []
        initnum = 0;
        for i in range(stage):
            initnum = initnum * 10 + N
        temp.append(initnum)
        for a in numarr:
            temp.append(a + N)
            temp.append(a - N)
            temp.append(a * N)
            temp.append(a // N)
        numarr = temp
        # numarr = list(set(numarr))
        if number in numarr:
            break
        # print(numarr)
        stage +=1
    if stage > 8:
        answer = -1
    else:
        answer = stage
    return answer