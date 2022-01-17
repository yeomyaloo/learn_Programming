def add_last(self,data):
    if self.head is None:
        self.add_first(data) #리스트가 비어있으면
    else:
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.current = Node(data,None)
        self.no += 1
        
