def solution(priorities, location):
    answer = 0
    order = []
    results = []
    priorities2 = [(v,i) for i,v in enumerate(priorities)]
    while len(priorities2) > 0:
        maxval = max(priorities2, key=lambda x: x[0])
        index = priorities2.index(maxval)
        results.append(priorities2[index])
        
        if index != 0 and index != len(priorities2) - 1 :
            div1 = priorities2[:index]
            div2 = priorities2[index+1:]
            div2 = div2 + div1
            priorities2 = div2
        else:
            del priorities2[index]
    resultIndex = [x[1] for x in results]
    answer = resultIndex.index(location) + 1
    return answer