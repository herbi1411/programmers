def solution(nums):
    answer = 0
    cases = getCases(nums)    
    primeNumbers = getPrimeNumbers(50000)
    
    for c in cases:
        if c in primeNumbers:
            answer+=1
    return answer


def getCases(nums):
    cases = []
    len_nums = len(nums)
    for i in range(len_nums-2):
        for j in range(i+1,len_nums-1):
            for k in range(j+1,len_nums):
                cases.append(nums[i]+nums[j]+nums[k])
    return sorted(cases)   


def getPrimeNumbers(num):
    primeNumbers = []
    temp = [1] * (num+1)

    temp[0] = 0
    temp[1] = 0
    
    for i in range(2,num+1):
        if temp[i] == 1:
            for j in range(i+i,num+1,i):
                temp[j] = 0
    
    for i in range(num):
        if temp[i] == 1:
            primeNumbers.append(i)
    
    return primeNumbers