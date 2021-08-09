n = int(input())
lst = []


for _ in range(n):
    lst.append(input())

lst= sorted(lst, key = len)

for i in lst:
    print(i)
