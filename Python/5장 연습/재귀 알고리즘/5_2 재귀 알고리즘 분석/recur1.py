#순수한 재귀 함수 구현하기

def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)
x = int(input('정수값을 입력하세요.: '))
recur(x)
