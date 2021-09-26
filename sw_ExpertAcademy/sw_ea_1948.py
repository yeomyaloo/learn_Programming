t = int(input())
#달과 날짜를 묶어서 딕셔너리로 넣어준다. 키값을 이용해서 접근하기 때문
days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:30}


for tc in range(1,t+1):
    m1, d1, m2, d2 = map(int,input().split())
    result = 0
    for i in range(m1,m2):
        # 달이 같은 경우
        if m1 == i:
            result += days[i] - d1 +1
        else:
            result += days[i]
    result += d2

    print(f'#{tc} {result}')
