import sys
input = sys.stdin.readline

n = int(input())
coin = [500,100,50,10,5,1]
charge = 1000-n
result = 0
for i in coin:
    result += charge//i
    charge = charge%i
print(result)

    
