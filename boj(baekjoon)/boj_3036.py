def gcd(a,b):
    while b!=0:
        n = a%b
        a = b
        b = n
    return a

n = int(input())
rings = list(map(int,input().split()))

for i in range(1, n):
    g = gcd(rings[0],rings[i])
    print(f"{rings[0]//g}/{rings[i]//g}")
