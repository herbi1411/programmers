import re
def solution(s):
    answer = []
    temp = s.split("},")
    result = []
    for row in temp:
        nlist = []
        temp2 = row.split(",")
        nlist = [int(re.sub(r'[^0-9]', '', str(val))) for val in temp2]
        result.append(nlist)
    result.sort(key = lambda x : len(x))
    for row in result:
        for val in row:
            if val in answer:
                continue
            else:
                answer.append(val)
    # print(result)
    # print(nlist)
    # answer = list(set(nlist))
    return answer