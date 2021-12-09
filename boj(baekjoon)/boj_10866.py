from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    command = list(input().split())

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] =='push_back':
        dq.append(command[1])
    elif command[0] =='pop_front':
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] =='pop_back':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] =='size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif command[0] =='front':
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    else:
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)
        
            
        
