<<<<<<< HEAD
# 증가하는 부분을 담고 그 담은 것을 if문으로  들어있나 확인하는 것?

import sys
input = sys.stdin.readline

a = list(input())
b = list(input())
lst = []

dp = [0 for i in range(1000)] #dp 테이블 초기화

for i in range(len(b)):
    for j in range(i):
        if b[i] < b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            lst.append(i)

if lst in a:
    print(len(lst))
=======
import sys
input = sys.stdin.readline

s1 = input().strip().upper()
s2 = input().strip().upper()

dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
>>>>>>> 7be1aa3385a4975f316f2fa918f3e4ee6cbc67c1
