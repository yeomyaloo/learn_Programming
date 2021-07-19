# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
    #정수값 x와 y의 최대 공약수를 반환
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

print("두 정숫값의 최대 공약수를 구합니다.")
x = int(input("첫 번째 정숫값을 입력하세요.: "))
y = int(input("첫 번째 정숫값을 입력하세요.: "))

print(f'두 정숫값의 최대 공약수는 {gcd(x,y)}입니다.')
