def solution(nums):
    answer = 0
    myset = set()
    
    for val in nums:
        myset.add(val)
    answer = len(myset)
    return min(answer, len(nums) // 2)