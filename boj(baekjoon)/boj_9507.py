import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1,1,2,4]       
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4])
    print(dp[n])
