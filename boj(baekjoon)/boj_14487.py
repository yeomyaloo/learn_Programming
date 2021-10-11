n=int(input())
vilige = list(map(int,input().split()))
vilige.sort(reverse=True)
result = 0
for i in range(n-1):
    result += vilige.pop()
print(result)
