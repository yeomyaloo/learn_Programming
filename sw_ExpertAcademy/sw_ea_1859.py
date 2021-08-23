T = int(input())

for j in range(T):
    n = int(input())
    lst = list(map(int,input().split()))
    last_lst=lst[-1] #1
    cnt = 0
    
    for i in range(len(lst)-1,-1,-1):
        if last_lst > lst[i]:
            cnt += last_lst-lst[i]
        else:
            last_lst = lst[i]
    print(f'#{j+1} {cnt}')
            
        
