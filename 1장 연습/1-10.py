print("a부터 b까지의 정수의 합을 구합니다.")
a = int(input("정수 a를 입력하세요."))
b = int(input("정수 b를 입력하세요."))

if a > b :
    a, b = b, a #a가 b보다 크다면 a에 b값을 b엔 a값을 넣어준다.

    
sum = 0
for i in range(a,b+1):
    if i < b:
        print(f"{i} + ", end = '') #i가 b보다 작은 경우 과정 출력 진행중인 값 뒤엔 +

    else:
        print(f"{i} = ", end = '') #i가 b보다 커서 결과를 대입하는 경우 최종 값 뒤에 = 
    sum += i

print(sum)
