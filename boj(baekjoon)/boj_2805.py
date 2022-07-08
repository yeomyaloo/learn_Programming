n, m = map(int,input().split())

tree = list(map(int,input().split()))
lt = 1
rt = max(tree)
res = 0
#자른 값과 남은 값이 큰 경우를... 이땐 남은 값이 더 큰 경우를 찾아야 하기에..lt를 증가!
 
while lt <= rt:
    mid = (lt+rt)//2
    s = 0
    for i in tree:
        if i >= mid:
            s+= i-mid
    if s >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
