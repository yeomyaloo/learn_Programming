#1938

a = int(input())
lst =[]

for i in range(1,a+1):
    if a % i == 0:
         lst.append(i)

lst.sort()

for i in lst:
    print(i, end=' ')
    
