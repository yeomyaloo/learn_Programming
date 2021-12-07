import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1].split(",")
    
    queue = deque(x)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0

    # 넣은 원소가 없을 때 빈 리스트를 돌려 준다. 
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
