def solution(name):
    answer = 0
    dp = [[("A" * len(name),0)]]

    while 1:
        if name == dp[-1][0]:
            break
        answer += 1
        nlist = []
        
        for word,cursor in dp[-1]:
        
            curword = word
            curcursor = cursor
            
            temp = curword[:]
            temp = list(temp)
            if temp[curcursor] == 'Z':
                temp[curcursor] = 'A'
            else:
                temp[curcursor] = chr(ord(temp[curcursor]) + 1)
            temp = ''.join(curword)
            nlist.append((temp,curcursor))
            
            temp = curword[:]
            temp = list(curword)
            # print((word,cursor), temp[curcursor])
            if temp[curcursor] == 'A':
                temp[curcursor] = 'Z'
            else:
                temp[curcursor] = chr(ord(temp[curcursor]) - 1)
            temp = ''.join(temp)
            nlist.append((temp,curcursor))

            if curcursor == len(name) - 1:
                nlist.append((curword,0))
            else:
                nlist.append((curword,curcursor+1))
            if curcursor == 0:
                nlist.append((curword,len(name)-1))        
            else:
                nlist.append((curword,curcursor-1))        

        dp.append(nlist)
        # print(nlist)
    return answer