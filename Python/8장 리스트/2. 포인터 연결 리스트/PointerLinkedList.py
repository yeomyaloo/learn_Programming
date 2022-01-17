#포인터로 연결 리스트 구현하기

class Node:
    def __init__(self,data):
        #초기화
        self.data = data
        self.next = next

#연결 리스트 클래스

class LinkedList:
    
    def __init__(self):
        #초기화
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드

    def __len__(self):
        # 연결 리스트의 노드 개수를 반환
        return self.no

def search(self,data):
    #data와 값이 같은 노드를 검색
    cnt = 0
    ptr = self.head

    while prt is not None:
        if ptr.data == data:
            self.current = ptr
            return cnt

        cnt += 1
        ptr = ptr.next
    return -1

def __contains__(self,data):
    #연결 리스트에 data가 포함되어 있는지 확
    return self.search(data >= 0

def add_first(self,data):
    #맨 앞에 노드 삽입
    ptr = self.head
    self.head = self.current = Node(data,ptr)
    self.no += 1


def add_last(self,data):
    if self.head is None:
        self.add_first(data) #리스트가 비어있으면
    else:
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.current = Node(data,None)
        self.no += 1
        
