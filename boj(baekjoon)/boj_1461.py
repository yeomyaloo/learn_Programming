n,m = map(int,input().split())
lst = list(map(int,input().split()))

p = []
minus = []
res = []

for i in lst:
    if i > 0:
        p.append(i)
    else:
        minus.append(i)

p.sort(reverse=True)
minus.sort()

max_v = 0
for i in lst:
    if abs(i) > abs(max_v):
        max_v = i

for i in range(0,len(p),m):
    if p[i]!=max_v:
        res.append(p[i])

for i in range(0,len(minus),m):
    if minus[i]!=max_v:
        res.append(minus[i])
answer = abs(max_v)
for i in res:
    answer+=abs(i*2)
print(answer)
