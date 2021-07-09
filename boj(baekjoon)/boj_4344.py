C = int(input()) #테스트 케이스의 개수
n =[]
for _ in range(C):
    n = list(map(int,input().split()))
    ave = sum(n[1:]) / n[0] #n[0]번째가 입력받은 학생의 수이기 때문에 이로 점수의 합(1번째 자리부터 학생시작)/n 해주면 평균이 나온다. 
    cnt =0
    for i in n[1:]:
        if i>ave:
            cnt += 1 #평균이 넘는 학생의 수를 구하기 위함

    print(str('%.3f' %round(cnt/n[0]*100,3)) +"%")
            
        
    
