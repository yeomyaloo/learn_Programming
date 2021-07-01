#체인법으로 해시 함수 구현하기


from __future__ import annotations

from typing import Any, Type

import hashlip

class Node:
    #해시를 구성하는 노드

    def __init__(self, key:Any, value: Any, next:Node) -> None:
        self.key = key #키
        self.value = value #값
        self.next = next #뒤쪽 노드 참조 
        
class ChainHash:
    #체인법으로 해시 클래스 구현

    def __init__(self,capacity: int) -> None:
        #초기화

        self.capacity = capacity
        self.table = [None]*self.capacity

    def hash_value(self,key:Any) -> int:
        #해시값을 구함
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib,sha256(str(key).encode()).hedigest(),16)%self.capacity)

def search(self, key:Any) -> Any:
    #키가 key인 원소를 검색해 값을 반환

    hash = self.hash_value(key) #검색하는 키의 해시값
    p = self.table[hash] #노드를 주목

    while p is not None: #검색 성공
        if p.key == key: 
            return p.value #뒤쪽 노드 주목
        p = p.next

    return None #검색 실패

def add (self,key:Any, value:Any)-> bool:
    #키가 key이고 값이 value인 원소를 추가
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
        if p.key == key:
            return False
        p = p.next

    temp = Node(key,value, self.table[hash])
    self.table[hash] = temp
    return True


def remove(self, key:Any) -> bool:
    #키가 key인 원소를 삭제

    hash = self.hash_value(key)
    p = self.table[hash]
    pp = None

    while p is not None:
        if p.key == key:
            if pp is None:
                self.table[hash] = p.next
            else:
                pp.next = p.next
            return True
        pp = p
        p = p.next
    return False

def dump(self) -> None:
    #해시테이블을 덤프
    for i in range(self.capacity):
        p = self.table[i]
        print(i, end='')
        while p is not None:
            print(f" -> {p.key} ({p.value})",end ='')
            p = p.next
        print()
