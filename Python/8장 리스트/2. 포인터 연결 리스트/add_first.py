def add_first(self,data):
    #맨 앞에 노드 삽입
    ptr = self.head
    self.head = self.current = Node(data,ptr)
    self.no += 1
    
