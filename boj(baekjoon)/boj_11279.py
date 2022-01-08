import heapq

n = int(input())


for _ in range(n):
    x = int(input())
    maxHeap = []
    if x != 0 :
        heapq.heappush(maxHeap,-x)
    else:
        try:
            print(heapq.heappop(maxHeap))

        except:
            print(0)
