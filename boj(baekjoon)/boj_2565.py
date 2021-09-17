import sys
input = sys.stdin.readline

n = int(input())
lst = []
lst_2 = []

dp = [0]*n
for _ in range(n):
    lst.append(list(map(int,input().split())))

# A순으로 정렬
lst.sort(key = lambda x:x[0])

#A순으로 정렬한 리스트목록에서 B만 리스트2에 담아 줌 
for i in range(n):
    lst_2.append(lst[i][1])

for i in range(n):
    for j in range(i):
        if lst_2[i] > lst_2[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

#입력받은 n에서 긴수열의 값을 빼준 것이 교차하는 전깃줄의     
print(n-max(dp))


    
