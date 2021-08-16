T = int(input())

for i in range(T):
    
    lst = list(map(int,input().split()))

    odd_nums = [num for num in lst if num % 2 == 1]

    print(f"#{i+1}",sum(odd_nums))

