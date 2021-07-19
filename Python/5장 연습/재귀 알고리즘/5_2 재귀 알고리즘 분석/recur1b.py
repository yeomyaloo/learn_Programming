#스택으로 재귀함수 구현하기(재귀를 제거)

from stack import Stack #Stack.py에서 스택 클래스 임포트
def recur(n):
#재귀를 제거한 recur()함
    s = Stack(n)

    while True:
        if n > 0 :
            s. push(n)        # n값을 푸시
            n = n - 1
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장한 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input("정수값을 입력해주세요.: "))
recur(x)
