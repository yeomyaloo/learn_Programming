#recur() 함수의 재귀 호출을 거꾸로 출력하기 

def recur(n):
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)
x = int(input('정수값을 입력하세요.: '))
recur(x)
