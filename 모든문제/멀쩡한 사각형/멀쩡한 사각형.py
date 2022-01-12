from math import *
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)
    
def solution(w,h):
    
    if w == 1 or h == 1:
        return 0
    
    answer = 0
    counter = 0
    gcd = GCD(w,h)
    
    gw = w // gcd
    gh = h // gcd
    
    for i in range(gw):
        updownRange = ceil((i+1) * gh / gw) - floor(i * gh / gw) 
        counter += updownRange
    answer = (w * h) - (counter * gcd)
    return answer