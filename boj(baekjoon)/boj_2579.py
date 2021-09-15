import sys
input = sys.stdin.readline

n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0]+s[1]
dp[2] = max(s[1]+s[2],s[0]+s[2])

#마지막의 경우엔 꼭 밟아주어야 하기 때문에 바로 직전의 것을 밟은 것과 안 밟은 것
for i in range(3,n):
    dp[i] = max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
print(dp[n-1])
