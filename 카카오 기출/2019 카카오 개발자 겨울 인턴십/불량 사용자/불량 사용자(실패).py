from collections import Counter

def makeDict(user_id):
    rdict = dict()
    for val in user_id:
        if len(val) not in rdict:
            rdict[len(val)] = []
        rdict[len(val)].append(val)
    return rdict

def solution(user_id, banned_id):
    answer = 0
    ulist = makeDict(user_id)
    answerlist = [0] * 9
    print(ulist)
    for banned in banned_id:
        if len(banned) not in ulist:
            continue
        for val in ulist[len(banned)]:
            flag = True
            for i in range(len(val)):
                if banned[i] == "*" or banned[i] == val[i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                ulist[len(banned)].remove(val)
                answer = 1
                print(val)
                answerlist[len(val)] += 1
        for val in answerlist:
            if val > 1:
                answer *= val
        print(answerlist)
    return answer