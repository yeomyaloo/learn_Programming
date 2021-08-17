#2029

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    c = a // b
    d = a % b
    print(f"#{i+1} {c} {d}")
