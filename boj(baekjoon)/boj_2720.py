import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    coin = [25, 10, 5,1]
    result = []
    c = int(input())
    for i in coin:
        result.append(c//i)
        c = c%i
    print(*result)
    
