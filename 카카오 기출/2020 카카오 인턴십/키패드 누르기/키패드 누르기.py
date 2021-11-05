def getDistance(x,y):
    if x == "*":
        x = 10
    elif x == "#":
        x = 12
    result = 0
    if x == 0 or y == 0:
        if x == y == 0:
            return 0
        x = max(x,y)
        y = 11
        # result += 1
    result += abs((x-1) // 3 - (y-1) // 3)
    result += abs(((x-1) % 3) - ((y-1) % 3))
    # print("======")
    # print((big-1) // 3 - (small-1) // 3)
    # print(abs(((big-1) % 3) - ((small-1) % 3)))
    # print(big,small,result)
    # print("======")
    return result

def solution(numbers, hand):
    answer = ''
    
    curL = "*"
    curR = "#"
    # curL = 0
    # curR = 0
    
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            curL = num
        elif num in [3,6,9]:
            answer += "R"
            curR = num
        elif num in [2,5,8,0]:
            tempL = getDistance(curL,num)
            tempR = getDistance(curR,num)
            # print("(",curL,num,") =",tempL," (",curR,",",num,")= ",tempR)
            if tempR > tempL:
                answer += "L"
                curL = num
            elif tempR < tempL:
                answer += "R"
                curR = num
            else:
                if hand == "right":
                    answer += "R"
                    curR = num
                else:
                    answer += "L"
                    curL = num
    return answer