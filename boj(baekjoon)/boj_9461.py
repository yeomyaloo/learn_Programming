a = [0 for i in range(101)]

a[1]= 1
a[2]= 1
a[3]= 1

for i in range(0,98):
    a[i + 3] = a[i] + a[i + 1]

t = int(input())
for i in range(t):
    n = int(input())
    print(a[n])
