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
