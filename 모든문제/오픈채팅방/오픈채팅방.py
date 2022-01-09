def solution(record):
    answer = []
    id_name = {}
    
    for r in record:
        r = r.split()
        if len(r) == 3:
            id_name[r[1]] = r[2]
    for r in record:
        r = r.split()
        if len(r) == 3:
            if r[0] == "Enter":
                answer.append(id_name[r[1]] + "님이 들어왔습니다.")
        elif len(r) == 2:
            if r[0] == "Leave":
                answer.append(id_name[r[1]] + "님이 나갔습니다.")
    return answer