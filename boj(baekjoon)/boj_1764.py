n, m = map(int,input().split())

d= {}

for i in range(n):
    name = input()
    d[name] = 1

for i in range(m):
    name = input()
    if name not in d:
        d[name] = 1
    else:
        d[name] = d[name] +1

res = []
 
for dic in d:
    if d[dic] == 2:
        res.append(dic)
res.sort()

print(len(res))
for r in res:
    print(r)
