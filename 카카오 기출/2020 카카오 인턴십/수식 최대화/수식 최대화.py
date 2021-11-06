import re
def solution(expression):
    answer = 0
    operator = ["*","-","+"]
    priority = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    operatorlist = list(re.sub(r'\d','',expression))
    nlist = list(map(int,re.findall(r'\d+',expression)))
    # print(nlist)
    # print(operator)
    
    for pt in priority:
        tnlist = nlist[:]
        toperatorlist = operatorlist[:]
        
        temp = [operator[i] for i in pt]
        for op in temp:
            dlist = []
            for i,opl in enumerate(toperatorlist):
                if op == opl:
                    dlist.append(i)
                    if op == "*":
                        tnlist[i+1] = tnlist[i] * tnlist[i+1]
                    elif op == "-":
                        tnlist[i+1] = tnlist[i] - tnlist[i+1]
                    elif op == "+":
                        tnlist[i+1] = tnlist[i] + tnlist[i+1]
            for d in dlist[::-1]:
                del tnlist[d]
                del toperatorlist[d]
        answer = max(answer,abs(tnlist[0]))
            
                    
                
    return answer