dp = [0,1,2]

for i in range(3, 1001):
    dp.append(dp[i-2] + dp[i-1])

n = int(input())
print(dp[n] % 10007)
