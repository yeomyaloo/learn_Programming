n = int(input()) # 설탕

cnt = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        cnt += n // 5 # 5로 나눈 몫 추력
        print(cnt)
        break
    n -= 3 # 입력받은 수를 3으로 계속 빼줘서 5의 배수가 될때까지 반복 5의 배수가 되면 if문을 통해서 
    cnt += 1 # 봉지에 개수 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력
