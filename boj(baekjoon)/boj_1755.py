o = {'8':'0', '5':'1', '4':'2', '9':'3', '1':'4', '7':'5', '6':'6', '3':'7', '2':'8', '0':'9'}
m, n = map(int, input().split())
r = []
for i in range(m, n+1):
    s = [str(i)]
    k = ""
    for j in s[0]:
        k += o[j]
    s.append(k)
    r.append(s)
    r = sorted(r, key=lambda x:x[1])
for i, j in enumerate(r):
    if (i+1)%10 == 0:
        print(j[0])
    else:
        print(j[0], end=" ")
