#1부터 n까지의 정수의 합 구하기

def sum_1ton(n):
    #1부터 n까지의 정수의 합

    s = 0
    while n > 0:
        s += n
        n -= 1

        print(f"s = {s}  n = {n}")
    return s

x = int(input("x의 값을 입력하세요.: "))

print(f"1부터 {x}까지의 정수의 합은 {sum_1ton(x)}입니다.")
