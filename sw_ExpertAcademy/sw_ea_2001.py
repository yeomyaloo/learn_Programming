T = int(input())

for t in range(1, T+1) : #1
    N, M  = map(int, input().split())
    lst = [ [0]*N for _ in range(N) ] 
    for i in range(N) : #2
        lst[i] = list(map(int, input().split()))
    die = [] #3
    for i in range(N-M+1) : #4
        for j in range(N-M+1) : #5
            count = 0
            for k in range(M) :
                for l in range(M) :
                    count += lst[i+k][j+l] #6
            die.append(count) #7
    die.sort() 
    print(f"#{t} {max(die)}") #8
