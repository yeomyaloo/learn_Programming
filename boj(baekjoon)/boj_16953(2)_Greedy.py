a,b = map(int,input().split())
cnt = 1 #cnt는 1부터 시작

while b!=a:
    cnt += 1
    temp = b #b의 값에서 값을 줄여나가며 진행한다
    if b%10 == 1: #홀수인 경우
        b //= 10 #몫만 취해서 끝의 1을 사라지게 한다.
    elif b%2 == 0:#짝수인 경우
        b //= 2 #2로 나눈다(2를 원래를 곱해주는 작업이니까)

    if temp == b:
        print(-1)
        break
else:
    print(cnt)
