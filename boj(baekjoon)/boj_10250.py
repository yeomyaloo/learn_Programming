#10250

t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    f = 0 
    no = 0
    if n % h == 0:
        f = h * 100 # 6층건물에 6번째 입장이면 601호 배정이기에 6층을 표현하기 위해 600을 입력받아야 함
        no = n//h #몫이 1이 나오기 때문
    else:
        f = (n%h)*100
        no = n//h +1
    print(f+no)
