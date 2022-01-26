import sys
import heapq
input = sys.stdin.readline


n,k = map(int,input().split())
bag = []
jewely = []
candidate = []
answer = 0

for _ in range(n):
    weight, price = map(int,input().split())
    heapq.heappush(jewely,[weight,price])

for _ in range(k):
    bag.append(int(input()))

bag.sort()

for i in bag:
    while jewely and i >= jewely[0][0]:
        weight, price = heapq.heappop(jewely)
        #최대힙을 사용 가격만 넣어주는 작업
        heapq.heappush(candidate,-price)

    #for문을 돌 때만, 그러니까 딱 가방수만큼만 최대힙으로 저장된 값이 answer에 더해짐
    if candidate:
        answer -= heapq.heappop(candidate)
print(answer)
