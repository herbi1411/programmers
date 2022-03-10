from collections import Counter
from math import *

def solution(str1, str2):
    answer = 0
    intersection = 0
    union = 0
    
    str1 = [str1[i].lower() + str1[i+1].lower() for i in range(len(str1) - 1) if str1[i].isalpha() == True and str1[i+1].isalpha() == True]
    str2 = [str2[i].lower() + str2[i+1].lower() for i in range(len(str2) - 1) if str2[i].isalpha() == True and str2[i+1].isalpha() == True]
    c1 = dict(Counter(str1))
    c2 = dict(Counter(str2))
    print(c1, c2)
    for key in c1:
        if key in c2:
            intersection += min(c1[key],c2[key])
            union += max(c1[key],c2[key])
        else:
            union += c1[key]
    for key in c2:
        if key not in c1:
            union += c2[key]
    if union == 0:
        return 65536
    else:
        print(intersection, union)
        return int(floor((intersection / union) * 65536))