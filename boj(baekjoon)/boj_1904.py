n= int(input())
dp = [0]*1000001
dp[1]=1
dp[2]=2

#1, 2값을 이미 알기에 3 = (3-1)+(3-2)이기 때문에 3부터 0부터 시작 아니여서 n+1까지
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%15746
    #15746을 나눈 나머지값으로 하라 했으니.
print(dp[n])