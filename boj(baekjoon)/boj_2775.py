#2775

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    p = [p for p in range(1,n+1)]
    
    for i in range(k):
        for j in range(1,n):
            p[j] += p[j-1]
    print(p[-1])
        

