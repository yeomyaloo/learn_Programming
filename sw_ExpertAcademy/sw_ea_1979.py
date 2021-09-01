t = int(input())


for tc in range(1,t+1):
    n, k = map(int,input().split())

    #리스트 내포 방식 활용 입력
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    
    for i in range(n):
        cnt = 0
        # 가로 검사
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            #벽을 만났을 때 그동안 쌓은 값이 k라면 단어가 들어갈 수 있는 조건 이기에 한 번더 살펴본다.
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0 #cnt를 초기화해주어야 함.
                
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0
    print(f'#{tc} {result}')
