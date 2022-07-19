from collections import deque

for _ in range(int(input())):
    n = int(input())
    s = input().split()

    dq = deque(s)
    res = deque(dq.popleft())
    while dq:
        now = dq.popleft()
        if now > res[0]:
            res.append(now)
        else:
            res.appendleft(now)
    print("".join(res))
        
