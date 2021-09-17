import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
r_lst = lst[::-1] #감소하는 부분 수열을 구하기 위함 뒤집어 저장

increase = [1 for i in range(n)]
decrease = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            increase[i] = max(increase[i],increase[j]+1)
        if r_lst[i] > r_lst[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] - 1

print(max(result))
