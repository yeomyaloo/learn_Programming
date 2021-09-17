from collections import Counter
t = int(input())

for tc in range(1,t+1):
    testcase = int(input())
    score = list(map(int,input().split()))

    #점수는 최대 100점    
    cnt = [0]*101

    #해당 점수가 몇번이나 나오는지 세기 위해 cnt 배열에 횟수 저장
    for i in score:
        cnt[i]+=1

    m = max(cnt)
    #최빈수가 여러개 존재할 때 점수가 더 큰 값을 출력해주기 위함 
    print(f'#{tc} {max([i for i, v in enumerate(cnt) if v == m])}')

    #enumerate
    #1. 반복문을 사용할 때 몇 번째 반복문인지를 확인할 때 사용
    #2. 인덱스 번호와 컬렉션의 원소를 튜플형태로 반환
    
    
