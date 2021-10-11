t = int(input())

for tc in range(1, t+1):
    n = int(input())
    lst = ''
    for i in range(n):
        alpha, num = input().split()
        lst += alpha*int(num)
    print(f'#{tc}')
    for i in range(0,len(lst),10):
        print(lst[i:i+10])

