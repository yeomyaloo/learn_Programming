n,k = map(int,input().split())

coins = []
answer = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse = True)

for i in coins:
    answer += k // i
    k = k%i
print(answer)
