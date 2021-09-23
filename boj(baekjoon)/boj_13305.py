import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split())) #도로 길이
price = list(map(int,input().split())) # 리터당 기름 가격

res = road[0]*price[0] #첫번째는 무조건 기름을 채우고 출발해야 하기 때문
m = price[0]
dist = 0

for i in range(1,n-1):
    if price[i] < m: #두 번째 가격이 첫 번째보다 작을 때
        res += m * dist
        dist = road[i] 
        m = price[i]
    else:
        dist += road[i]
    if i == n-2:
        res += m*dist
print(res)
