#11053

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int,input().split()))

#DP를 위한 1차원 DP테이블 초기화
dp = [1]*n

#가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행.
for i in range(1,n):
    for j in range(0,i):
        if a_list[j] < a_list[i]:
            dp[i] = max(dp[i],dp[j] +1)
print(max(dp))
