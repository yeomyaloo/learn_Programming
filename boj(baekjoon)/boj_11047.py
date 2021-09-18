import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
result = 0

for _ in range(n):
     coin.append(int(input()))
     
coin.sort(reverse = True)

for i in coin:
    if k == 0:
        break

    #coin에 담겨있는 돈(k에서 나눌 돈)이 k보다 큰 경운 컨티뉴
    if i>k:
        continue
    result += k//i
    k %= i
print(result)
