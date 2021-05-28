import random

n = int(input("난수의 개수를 입력하세요.: "))


for _ in range(n):
    r = random.randint(10, 99) #10에서 99 사이의 난수 n개 생성
    print(r, end =' ')

    if r == 13:
        print("\n13이 나와 프로그램을 중단합니다.")
        break

else:
    print(f"\n{n}개의 난수를 생성하여 난수 생성을 종료합니다.")
