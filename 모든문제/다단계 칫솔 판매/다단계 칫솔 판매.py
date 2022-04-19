def solution(enroll, referral, seller, amount):
    answer = []
    enroll.insert(0,'-')
    edict = {name: i for i, name in enumerate(enroll)}
    parent = [-1] * len(edict)
    answer = [0] * len(edict)
    for i, ref in enumerate(referral):
        parent[i + 1] = edict[ref]
    
    for sell, amt in zip(seller, amount):
        sell = edict[sell]
        forparent = amt * 100 / 10
        forme = amt * 100 - forparent
        answer[sell] += forme
        me = sell
        while parent[me] >= 0:
            temp = forparent
            forparent //= 10
            forme = temp - forparent
            me = parent[me]
            answer[me] += forme
            if forparent == 0:
                break
        
    return answer[1:]