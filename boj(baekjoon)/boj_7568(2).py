N = int(input())

n_list = []
for _ in range(N):
    x,y = map(int, input().split())
    people.append((x, y))

for c in n_list : 
    rank = 1 
    
    for n in n_list:
        if (c[0]!=n[0]) & (c[1]!=n[1]): 
            if (c[0]<n[0]) & (c[1]<n[1]): 
                rank += 1
            
    print(rank)
