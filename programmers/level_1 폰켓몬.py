def solution(nums):
    answer = 0
    n = len(nums)//2
    a = len(set(nums))
    if n > a:
        return a
    else:
        return n
