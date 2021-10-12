t = int(input())
for tc in range(1, t+1):
    
    l,u,x = map(int,input().split())
    if x > u:
        result = -1
    elif x < l :
        result = l-x
    elif x > l and x < u:
        result = 0
    print(f'#{tc} {result}')
    
