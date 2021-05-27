print("a부터 b까지의 정수의 합을 구합니다.")

a = int(input())
b = int(input())

if a > b :
    a, b = b, a #a가 b보다 크다면 a에 b값을 b엔 a값을 넣어준다.
sum = 0

for i in range(a,b+1):
    sum += i

print(f"{a}부터 {b}까지의 정수의 합은 {sum}입니다.")
