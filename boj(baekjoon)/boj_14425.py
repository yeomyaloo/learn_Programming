n, m =map(int,input().split())

s1 = [input() for _ in range(n)]
s2 = [input() for _ in range(m)]
cnt = 0


for s in s2:
    if s in s1:
        cnt += 1
print(cnt)
