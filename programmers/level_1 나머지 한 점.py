import collections
 
def solution(v):
    answer = []
    for i in zip(*v):
        #unzip해주어 진행 
        y = collections.Counter(i)
        answer.extend([i for i in y if y[i] == 1])
        #원소를 그대로 (리스트 형태가 아닌) 넣기 위해서 extend를 사용한다.
 
    return answer
