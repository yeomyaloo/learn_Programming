from itertools import combinations 
def sosu(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2,(num//2)+1):
            if num % n == 0:
                return False
        return True
    
def solution(nums):
    answer = 0 
    cmb = list(combinations(nums,3)) #nums에 있는 모든 원소를 3개씩 조합
    for i in cmb:
        #주어진 조합의 합이 소수가 되는지 판별하는 것 True를 받으면 +1
        if sosu(sum(i)):
            answer += 1
    return answer
