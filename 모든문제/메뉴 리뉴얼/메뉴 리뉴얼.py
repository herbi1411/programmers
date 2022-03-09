from itertools import combinations

def solution(orders, course):
    orders = [sorted(row) for row in orders]
    answer = []
    for n in course:
        temp = dict()
        for (i, row) in enumerate(orders):
            comb = list(combinations(row,n))
            comb.sort()
            for row2 in orders[i+1:]:
                comb2 = list(combinations(row2,n))
                comb2.sort()
                for t in comb2:
                    if t in comb:
                        if t not in temp:
                            temp[t] = 0
                        temp[t] += 1
        if len(temp) == 0:
            continue
        maxval = max(temp.values())
        for key,val in temp.items():
            if val == maxval:
                answer.append("".join(key))
    answer = list(answer)
    answer.sort()
    return answer