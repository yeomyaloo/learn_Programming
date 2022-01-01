from itertools import permutations
def solution(numbers):
    a = set() #중복을 방지하기 위해서 set으로 설정
    
    #순열을 사용해서 사용가능한 조합을 모두 찾아준 뒤 진행한다.
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    a -= set(range(0,2))
    for i in range(2,int(max(a)**0.5)+1):
        a -= set(range(i*2,max(a)+1,i))
    
    
    return len(a)
