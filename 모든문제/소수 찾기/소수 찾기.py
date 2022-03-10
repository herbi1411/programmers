from itertools import permutations
import math
def isprime(num):
    if (num < 2):
        return 0
    for i in range(2,int(math.sqrt(num) + 1)):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    nums = set()
    for n in range(1,len(numbers) + 1):
        nlist = list(set([int(''.join(a)) for a in list(permutations(numbers,n))]))
        nums.update(nlist)
    for num in nums:
        if isprime(num):
            answer += 1
    return answer