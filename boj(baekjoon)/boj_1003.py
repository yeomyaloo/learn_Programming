<<<<<<< HEAD
#0출력 1출력 횟수



T = int(input())
count_zero = 0
count_one = 0

for i in range(T):
    n = int(input())    
    for j in range(n):
        if n == 0:
            count_zero += 1

        elif n == 1:
            count_one += 1

        else:
            fibo(n-1) + fibo(n-2)

    print(count_zero, count_one)
=======
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
    
>>>>>>> de064b91e7cdacb2c62d82952961dabece9734c5
