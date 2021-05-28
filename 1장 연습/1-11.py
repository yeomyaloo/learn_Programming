print("a부터 b까지의 정수의 합을 구합니다.")
a = int(input("정수 a를 입력하세요."))
b = int(input("정수 b를 입력하세요."))

if a > b :
    a, b = b, a #a가 b보다 크다면 a에 b값을 b엔 a값을 넣어준다.

    
sum = 0
for i in range(a,b):
    print(f"{i} + ", end = '')
    sum += i

print(f"{b} = ", end = '')
sum += b
print(sum)
