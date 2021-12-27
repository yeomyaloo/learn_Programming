from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1)) # a부터 시작하는데 a부터 cnt가 1이기에 a,1을 큐에 넣어준다.

while q:
    now, cnt = q.popleft()
    if now == b:
        print(cnt)
        break
    elif now > b:
        continue
    q.append((int(str(now)+"1"),cnt+1))
    q.append((now*2,cnt+1))
else:
    print(-1)
