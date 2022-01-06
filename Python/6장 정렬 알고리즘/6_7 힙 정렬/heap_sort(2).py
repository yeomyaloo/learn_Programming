# heapq 모듈을 사용해서 힙 정렬

import heapq

def heap_sort(a):
    heap = []
    for i in a:
        heapq.heappush(heap,i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

        
print("힙 정렬을 수행합니다.")
num = int(input("원소 수를 입력하세요:"))
x = [None] * num
for i in range(num):
    x[i] =int(input(f"x[{i}]: "))
heap_sort(x)

print("오름차순으로 정렬했습니다.")
for i in range(num):
    print(f"x[{i}] = {x[i]}")
