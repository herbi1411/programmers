def solution(id_list, report, k):
    arr = [[0 for _ in range(len(id_list))] for __ in range(len(id_list))]
    answer = [0] * len(id_list)
    id_dict = {}
    for (i,id) in enumerate(id_list):
        id_dict[id] = i
    for val in report:
        a,b = val.split()
        arr[id_dict[b]][id_dict[a]] = 1
    for a in id_list:
        if sum(arr[id_dict[a]]) >= k:
            for (i,val) in enumerate(arr[id_dict[a]]):
                if val == 1:
                    answer[i] += 1            
    return answer