import sys
input = sys.stdin.readline

n = int(input())
a1 = list(map(int,input().split()))
a1.sort()
m = int(input())
a2 = list(map(int,input().split()))

def binary_search(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end)//2
        if a1[mid] == target:
            return True
        if target < a1[mid]:
            end = mid - 1
        elif target > a1[mid]:
            start = mid + 1
for i in range(m):
    if binary_search(a2[i]):
        print(1)
    else:
        print(0)
    
            
