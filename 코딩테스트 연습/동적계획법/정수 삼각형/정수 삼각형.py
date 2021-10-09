def solution(triangle):
    answer = 0
    row = triangle[-1]
    for crow in triangle[-2::-1]:
        temp = []
        for i,val in enumerate(crow):
            temp.append(max(row[i],row[i+1])+val)
        row = temp
    answer = row[0]

    return answer