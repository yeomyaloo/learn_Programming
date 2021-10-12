a = ['a','e','i','o','u']
t = int(input())

for tc in range(1,t+1):
    s = list(input())
    print(f'#{tc}', end=" ")
    for i in s:
        if i not in a:
            print(i, end='')
    print()
        
