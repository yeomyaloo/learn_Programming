n = int(input())
card = list(map(int,input().split()))

m = int(input())
a = list(map(int,input().split()))
for i in a:
    if i in card:
        print(1, end= " ")
    else:
        print(0, end= " ")
