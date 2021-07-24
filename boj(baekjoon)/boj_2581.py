M = int(input())
N = int(input())

mn_list = []
for i in range(M, N+1):
    cnt = 0
    
    if i > 1 : #1은 소수가 아니기 때문에 
        for j in range(2, i): #소수 판별기
            if i % j == 0:
                cnt += 1
                break  #소수가 아닐 땐 for문 중단
        if cnt == 0:
            mn_list.append(i)   #소수일 땐 리스트에 항목 append해주기
            
if len(mn_list) > 0 : #리스트에 항목이 있다면 len이 0보다 크다
    print(sum(mn_list)) # 전부 더한 값을 sum 함수로 더해줌
    print(min(mn_list)) #min 함수를 사용해서 리스트 내의 제일 작은 값을 출력해
else:
    print(-1)
