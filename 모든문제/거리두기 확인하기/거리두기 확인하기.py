import math
def solution(places):
    answer = []
    for place in places:
        result = 1
        player = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    player.append((i,j))
        for i in range(len(player)):
            for j in range(i+1,len(player)):
                x1,y1 = player[i]
                x2,y2 = player[j]
                if abs(x1-x2) + abs(y1-y2) == 1:
                    result = 0
                elif abs(x1-x2) + abs(y1-y2) == 2:
                    bx = max(x1,x2)
                    sx = min(x1,x2)
                    by = max(y1,y2)
                    sy = min(y1,y2)
                    if (sy == by):
                        if place[sx + 1][sy] != 'X':
                            result = 0
                    elif(sx == bx):
                        if place[sx][sy + 1] != 'X':
                            result = 0
                    else:
                        if x1 < x2:
                            if y1 < y2:
                                if place[x1][y1 + 1] != 'X' or place[x1 + 1][y1] != 'X':
                                    result = 0
                            else:
                                if place[x1][y1 - 1] != 'X' or place[x1 + 1][y1] != 'X':
                                    result = 0
                        else:
                            if y1 < y2:
                                if place[x1 - 1][y1] != 'X' or place[x1][y1 + 1] != 'X':
                                    result = 0
                            else:
                                if place[x1 - 1][y1] != 'X' or place[x1][y1 + 1] != 'X':
                                    result = 0
                if result == 0:
                    break
            if result == 0:
                break
            
        answer.append(result)
                    
    return answer