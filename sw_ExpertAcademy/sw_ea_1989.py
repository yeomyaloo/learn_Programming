#1989

T = int(input())

for i in range(T):
    s = input()
    if s == s[::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
