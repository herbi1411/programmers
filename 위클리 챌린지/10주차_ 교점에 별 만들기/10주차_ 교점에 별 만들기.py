def solution(line):
    answer = []
    points = []
    
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            findPoint(line[i],line[j],points)
            
    # print(points)
    minx = min(points, key= lambda x: x[0])[0]
    maxy = max(points, key= lambda x: x[1])[1]
    maxx = max(points, key = lambda x: x[0])[0]
    miny = min(points, key = lambda x: x[1])[1]
    
    xsize = maxx-minx + 1
    ysize = maxy-miny + 1
    
    # print(xsize,ysize)
    matrix = [[0] * xsize for _ in range(ysize)]
    for x,y in points:
        matrix[maxy-y][x-minx] = 1
        
    # print(matrix)
    for row in matrix:
        rstring = ""
        for val in row:
            if val == 0:
                rstring += "."
            elif val == 1:
                rstring += "*"
        answer.append(rstring)
        # print(answer)
    # print(answer)
    return answer

def findPoint(p1,p2,arr):
    
    a1,b1,c1 = p1
    a2,b2,c2 = p2
    x = 0
    y = 0
    if (a1 == 0 and a2 == 0) or (b1 == 0 and b2 == 0) or (b1 != 0 and b2 != 0 and a1/b1 == a2 /b2):
        x = -1.1
        y = -1.1
    elif a1!= 0 and b1!=0 and a2!= 0 and b2!=0 and (a1/b1 != a2/b2):
        a1 *= b2
        c1 *= b2
        a2 *= b1
        c2 *= b1
        x = (c2-c1) / (a1-a2)
        y = -(c1 + a1 * x) / (b1 * b2)
    elif a1 == 0: # 0*x + b1*y + c1 =  0 // a2x + b2y + c2 = 0
        y = -(c1 / b1)
        x = -(c2 + y* b2) / a2
    elif a2 == 0:
        y = -(c2 / b2)
        x = (c1 - y*b1) / a1
    elif b1 == 0: # a1*x + 0 + c1 = 0 // a2x + b2y + c2 = 0
        x = - (c1/a1)
        y = -(c2 + a2 * x) / b2     
    elif b2 == 0:
        x = - (c2/a2)
        y = -(c1 + a1 * x) / b1
    else:
        print("unreachable code")
    if x.is_integer() and y.is_integer():
        # print("========")
        # print(p1)
        # print(p2)
        # print(a1,b1,c1)
        # print(a2,b2,c2)
        # print(x,y)
        # print("========")
        arr.append((int(x),int(y)))