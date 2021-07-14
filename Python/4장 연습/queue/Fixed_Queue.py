#고정 길이 큐 클래스 FixedQueue 구현하기
from typing import Any

class FiexQueue:

    class Empty(Exception):
        #비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        #꽉 차있는 FixedQueue에서 인큐할 때 내보내는 예외 처리
        pass

    def __init__(self,capacity: int) -> None:
         #큐 초기화
         self.no = 0 #현재 데이터 개수 
         self.front = 0 #맨 앞 원소의 커서
         self.rear = 0 #맨 끝 원소의 커서
         self.capacity = capacity #큐의 크기 스택에서는 스택크기로 쓰였다.
         self.que = [None] * capacity

    def __len__(self) -> int:
         #큐에 있는 모든 데이터 개수를 반환
         return self.no
    def is_empty(self) -> bool:
        #큐가 비어있는지 판단
        return self.no <= 0
        
    def is_full(self) -> bool:
        #큐가 꽉 차있는지 판단
        self.no >= self.capacity

    def enque(self, x:Any) -> None:
        if self.if_full():
            raise FixedQueue.Full #큐가 가득 차 있는 경우 예외 처리 발생
        self.que[self.rear] = x #입력받은 x값을 현제 rear 위치에 넣어준다.
        self.rear += 1 #rear을 뒤로 한 칸 보내준다.
        self.no += 1 #인큐 해줬으니 큐에 쌓여 있는 데이터 개수를 1개 늘려준다
        #큐의 크기인 capacity와 같을 경우 rear을 맨 앞 인덱스로 돌려준다. 
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> None:
        if self.if_empty():
            raise FixedQueue.Empty #큐가 비어 있는 경우 예외 처리 발생

        x = self.que[self.front]
        self.front += 1 #rear을 뒤로 한 칸 보내준다.
        self.no += 1 #인큐 해줬으니 큐에 쌓여 있는 데이터 개수를 1개 늘려준다.
        
        # 큐의 크기인 capacity와 같을 경우 front를 1 증가시켜 배열의 맨 앞 인덱스인 0으로 되돌려 준다.
        if self.front == self.capacity:
            self.front = 0

   def peek(self)->Any:
        if.self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self,value:Any) -> Any:
        
        #쌓여있는 데이터 개수만큼 for문 반복
        for i in range(self.no):
            #큐의 맨 앞 원소부터 스캔을 시작하기 위함
            idx = (i +self.front) % self.capacity 
            #검색 성공
            if self.que[idx] == value:
                return idx
        #검색 실패
        return -1
    def count(self,value:Any) -> bool:
        #큐에 있는 value의 개수 반환
        c = 0
        for i in range(self.no):
            idx = (i+self.front) % self.capacity
            if self.que[idx] == value:
                c+=1
        return c
    def __contains__(self, value:Any) -> bool:
        #큐에 value가 있는지 판단
        return self.count(value)
    def clear(self) -> None:
        #큐의 모든 데이터를 비움
        self.no = self.front = self.rear =0

    def dump(self) -> None:
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            for i in range(self.no):
                print(self.que[i+self.front]%self.capacity,end="")
            print()
