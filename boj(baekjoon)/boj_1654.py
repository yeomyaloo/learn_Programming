k, n = map(int,input().split())
line = [int(input()) for _ in range(k)]

lt = 1
rt = max(line)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    s = 0
    for i in line:
        s += i//mid
    if s >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1
print(res)
