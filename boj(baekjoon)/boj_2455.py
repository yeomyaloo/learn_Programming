train =  [0] * 4

for i in range(4):
    OUT, IN = map(int,input().split())
    if i == 0:
        train[0] += IN
    train[i] = train[i-1] - OUT + IN

print(max(train))
