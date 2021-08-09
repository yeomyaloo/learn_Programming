import sys

n = int(sys.stdin.readline())
xy_lst = []
for i in range(n):
    xy_lst.append(list(map(int, sys.stdin.readline().split())))
xy_lst.sort(key=lambda x:(x[0],x[1]))
for i in xy_lst:
    print(i[0],i[1])
