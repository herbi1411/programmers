def solution(genres, plays):
    answer = []
    genreDic = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        combination = (i,play)
        if genre in genreDic:
            genreDic[genre].append(combination)
        else:
            genreDic[genre] = [combination]
    genresVal = list(genreDic.values())
    genresVal.sort(key=lambda x: -sum([val[1] for val in x]))
          
    for row in genresVal:
        row.sort(key=lambda x: (-x[1],x[0]))
        
    for row in genresVal:
        answer.append(row[0][0])
        if len(row) >= 2 :
            answer.append(row[1][0])
    print(genresVal)
    return answer