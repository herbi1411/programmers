def solution(s):
    answer = len(s)
    
    for i in range(1,len(s)):
        tempstr = ''
        index = 0
        ch = s[index:index+i]
        dup = 0
        
        while index < len(s):
            
            if index + i > len(s):
                if dup > 1:
                    tempstr += str(dup)
                tempstr += ch
                tempstr += s[index:]
                
            elif index + i == len(s):
                if ch == s[index:index+i]:
                    dup += 1
                    tempstr += str(dup)
                    tempstr += ch
                    dup = 1
                else:
                    if dup > 1:
                        tempstr += str(dup)
                    tempstr += ch
                    tempstr += s[index:]
                    
            elif ch == s[index:index+i]:
                dup += 1
                
            else:
                if dup != 1:
                    tempstr += str(dup)
                    dup = 1
                tempstr += ch
                ch = s[index:index+i]
            index += i
        
        # print(i,tempstr)
        answer = min(answer,len(tempstr))
                    
    return answer