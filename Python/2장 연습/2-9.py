#1000이하의 소수를 나열하기(알고리즘 개선1)

counter = 0 # 나눗셈 횟수 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2 # 2는 소수 prime[0] = 2 / 배열값에 저장
ptr += 1

prime[ptr] = 3 # 3는 소수 prime[1] = 2 / 배열값에 저장
ptr += 1



for n in range(5, 1001, 2): #홀수만을 대상으로 설정 5,7,9,,,,,
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2 #이미 소수 2와 3이 들어가 있기 때문에 counter에 +2를 해준다
        
        if n % prime[i] == 0: # 나누어 떨어지는 경우 소수가 아님
            break
        
        else:
            prime[ptr] = n 
            ptr += 1
            counter += 1

for i in range(ptr):
    print(prime[i])

print(f"나눗셈을 실행한 횟수: {counter}")
