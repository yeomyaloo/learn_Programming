def gcd(a, b):
    c = 1
    while c != 0:
        c = a % b
        a = b
        b = c

    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)


n = int(input())

for _ in range(n):
    a, b = map(int, input().split(" "))
    
    if a > b:
        print(int(lcm(a, b)))
    
    else:
        print(int(lcm(b, a)))
