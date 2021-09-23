import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
sum = [a[0]]
#sum의 0번째 인덱스에는 비교를 위해 a[0]를 넣어준다.

for i in range(n-1):
    sum.append(max(sum[i]+a[i+1], a[i+1]))
        
print(max(sum))     
    
