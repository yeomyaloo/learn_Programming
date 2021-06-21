#1000이하의 소수를 나열하기

count = 0

for n in range(2, 1001): #2이상 1,000이하의 소수
    for i in range(2,n): 
        count += 1
        if n%i == 0:
            break
        else:
            print(n)

print(f"나눗셈을 실행한 횟수: {count}")
