from itertools import combinations
def solution(numbers):
    #비어있는 집합 자료형을 만들어서 결과를 받을 것이다.
    answer = set()
    
    # 넘버 리스트 안에 2개의 요소로 구할 수 있는 모든 조합을 반환하는 함수
    for i in list(combinations(numbers,2)):
        #반환 받은 조합 i(1,1이라면) 둘을 더해주어야 하니까 더한값을 돌려준다.
        answer.add(sum(i))
        
    return sorted(answer)
