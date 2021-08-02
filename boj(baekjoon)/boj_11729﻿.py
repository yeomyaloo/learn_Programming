def hanoi(n,a,b,c): #n = 원반의 수, a = 1번 봉/ b = 2번 봉 / c = 3번 봉
    if n == 1: #원반이 1개인 경우
        print(a,c) #1번봉에 있다 3번 봉으로 가는 것을 의미
    else:
        hanoi(n-1,a,c,b) #맨 아래 봉을 제외하고 계속 진
        print(a,c)
        hanoi(n-1,b,a,c)


n = int(input())
print(2**n-1)
hanoi(n,1,2,3)
