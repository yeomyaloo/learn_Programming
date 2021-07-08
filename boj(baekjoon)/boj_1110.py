N = num = int(input())
count = 0

while True:
    ten = N //10 #10의자리 
    one = N % 10 #1의 자리
    sum = ten + one #입력받은 N의 10의자리 1의자리 두 수의 더하기
    count += 1 #사이클 횟수 증가
    N = int(str(N%10)+str(sum%10)) #가장 오른쪽 자리에 있는 것들을 또 더해주기(즉, 1의자ㄹ)
    if(num==N):
        break #만약 처음 입력받은 N값 즉, num(여기엔 초기N값이 저장되어 있음)과 N이 같다면 프로그램 종료
print(count)        
