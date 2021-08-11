n = int(input())

lst = list(map(int,input().split()))

n_lst=list(sorted(set(lst)))
n_lst = {n_lst[i]:i for i in range(len(n_lst))}

for i in lst:
    print(n_lst[i], end=" ")
