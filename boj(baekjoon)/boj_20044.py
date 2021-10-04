n = int(input())
w = list(map(int,input().split()))

w.sort()
result = []

for i in range(n):
    result.append(w[i]+w[2*n-i-1])

            
print(min(result))
