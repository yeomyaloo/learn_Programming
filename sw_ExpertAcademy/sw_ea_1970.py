t = int(input())

coin = [50000,10000,5000,1000,500,100,50,10]


for tc in range(1,t+1):
    n = int(input())
    result = []
    for i in coin:
        result.append(n//i)
        n = n % i

    print(f'#{tc}')
    print(*result)

        
