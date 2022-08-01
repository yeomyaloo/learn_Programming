n, m = map(int,input().split())

d= {}
res = []

for i in range(n):
    name = input()
    d[name] = 1

for i in range(m):
    name = input()
    if name in d:
        res.append(name)
res.sort()
print(len(res))
for r in res:
    print(r)
