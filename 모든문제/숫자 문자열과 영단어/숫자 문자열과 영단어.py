def solution(s):
    numdict = {"one":'1',"two":'2',"three":'3',"four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0",}
    answer = 0
    answer_str = ''
    idx = 0
    while (idx < len(s)):
        if ord('0')<=ord(s[idx])<=ord('9'):
            answer_str += s[idx]
            idx+=1
        else:
            if s[idx:idx+3] in ["one","two","six"]:
                answer_str += numdict[s[idx:idx+3]]
                idx += 3
            elif s[idx:idx+4] in ["zero","four","five","nine"]:
                answer_str += numdict[s[idx:idx+4]]
                idx += 4
            elif s[idx:idx+5] in ["three","seven","eight"]:
                answer_str += numdict[s[idx:idx+5]]
                idx += 5
    answer = int(answer_str) 
    return answer