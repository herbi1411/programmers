import re

def solution(new_id):
    answer = ''
    
    #stage 1
    s1 = new_id.lower()
    
    #stage 2
    s2 = ''
    for a in s1:
        if ord('a')<=ord(a)<=ord('z') or ord('0')<=ord(a)<=ord('9') or a == "-" or a == "_" or a == ".":
            s2 += a
    
    #stage 3
    s3 = re.sub("[.][.]+",".",s2)
    
    #stage 4
    s4 = s3
    if len(s4) >0 and s4[0] == ".":
        s4 = s4[1:]
    if len(s4) >0 and s4[-1] == ".":
        s4 = s4[:-1]
        
    #stage 5
    s5 = s4
    if len(s5) == 0:
        s5 = "a"
    
    #stage 6
    s6 = s5
    if len(s6) >= 16:
        s6 = s6[:15]
    if len(s6) >0 and s6[-1] == ".":
        s6 = s6[:-1]
    
    #stage 7
    s7 = s6
    if len(s7) <= 2:
        fin = s7[-1]
        while(len(s7) < 3):
            s7 += fin
            
    answer = s7
    
    return answer