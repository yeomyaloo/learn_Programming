n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

ser_lst=set(lst)
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)
