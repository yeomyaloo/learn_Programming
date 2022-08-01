#1269

a, b = map(int,input().split())
num1 = set(map(int,input().split()))
num2 = set(map(int,input().split()))


print(len(num1-num2)+len(num2-num1))
