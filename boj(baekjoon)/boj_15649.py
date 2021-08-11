#15649

n, m = map(int,input().split())
lst =[]

for i in range(1,n+1):
    for j in range(1,m+1):
        if i >= 1 and j < 0: 
            lst.append(i)
           
