t = 10

for tc in range(1, t+1):
    tastcase_num = int(input())
    result = 0
    a,b = map(int,input().split())
    result = a**b

    print(f'#{tc} {result}')
