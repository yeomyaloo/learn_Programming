from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    q = deque(list(map(int,input().split())))
    cnt = 0

    while q:
        maxQ = max(q)
        front = q.popleft()
        m -= 1

        if maxQ == front:
            cnt += 1
            if m < 0 :
                print(cnt)
                break
        else:
            q.append(front)
            if m < 0 :
                m = len(q) - 1 
    
