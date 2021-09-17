t = int(input())

for tc in range(1,t+1):
    P, Q, R, S, W = map(int,input().split())
    # P = a사 1리터당 요금
    # Q = b사 R리터 이하 요금
    # R = b사 R리터부터 요금
    # S = b사 R리터부터 1리터당 요금
    # W = 종민이의 한 달간의 사용하는 수도 양
    A = P * W
    if W < R: #한달 사용 수도양이 기준치보다 작은 경우
        B = Q
    else:
        B = Q+((W-R)*S)
    print(f"#{tc} {min(A,B)}")
        
