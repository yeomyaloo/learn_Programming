t = int(input())

for i in range(t):
    n = int(input())
    
    # n = 0 일때, zero 1번 호출 one 0번 호출
    zero = 1
    one = 0
    tmp = 0

    for _ in range(n):
        tmp = one
        one = one+zero
        zero = tmp
    print(zero, one)
    
