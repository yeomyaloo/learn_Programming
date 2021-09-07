#n초 동안 이동한 거리를 계산하는 프로그램

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    total = 0
    speed = 0
    
    for nc in range(n):
        a = list(map(int,input().split()))

        # 가속일 때
        if a[0] == 1:
            speed += a[1]
            
         # 감속일 때
        elif a[0] == 2:
            #현재 속도보다 감속할 속도가 더 큰 경우 속도는 0이 된다.
            if speed < a[1]:
                speed = 0
            else:
                speed -= a[1]

        total += speed
    print(f"#{tc} {total}")
