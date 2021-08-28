#1984

T = int(input())
lst = []

for i in range(1,T+1):
    lst = list(map(int,input().split()))
    lst.sort()
    lst.pop(0)
    lst.pop(-1)
    print(f'#{i} {round(sum(lst)/8)}')
