from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    b = deque([0 for _ in range(bridge_length)])
    w = 0 #다리 위의 무게 
    q = deque(truck_weights)
    
    while len(q) > 0 or w > 0:
        #지워주는 작업부터 시작.
        # 0으로 초기화 해주어서 popleft의 문제가 생기지 않는 것. 
        removeTruck = b.popleft() 
        w -= removeTruck
        
        if len(q) and q[0] + w <= weight:
            x = q.popleft()
            w += x
            b.append(x)
        else:
            b.append(0) # 다리길이 유지를 위함 
                        # 다음에 다리길이를 하나 pop하기 때문
        
        time += 1
    return time
