n = int(input())
for i in range(n):
    print(" "*i,end="")
    print("*"*(2*(n-i)-1))
for j in range(n-2,-1,-1):
    print(" "*j,end="")
    print("*"*(2*(n-j)-1))
    
