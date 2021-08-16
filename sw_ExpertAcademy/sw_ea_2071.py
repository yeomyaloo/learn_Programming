T = int(input())
lst = []

for i in range(T):
    lst = list(map(int,input().split()))
    ave = round(sum(lst)/10)
    print(f'#{i+1}',ave)
