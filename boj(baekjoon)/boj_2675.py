#2675


T = int(input())

for i in range(T):
    n, s = input().split()
    t = ''
    for i in s:
        t += int(n)*i
    print(t)



