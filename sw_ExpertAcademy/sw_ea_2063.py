N = int(input())
lst = []


lst = list(map(int,input().split()))
middle = len(lst)//2
lst.sort()
print(lst[middle])
