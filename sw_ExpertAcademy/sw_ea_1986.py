T = int(input())


for j in range(1,T+1):
    N = int(input())
    result = 0
    for i in range(1,N+1):
        if i%2 == 0:     
            result -= i  
        elif i%2 == 1:  
            result += i
    print(f'#{j} {result}')

