from collections import deque


def BFS():
    q = deque()
    q.append(n) #현재 수빈이의 위치를 넣어서 확인해줘야 한다.
    while q:
        x = q.popleft()
        if x == k:
            print(time[x])
            return
        for next_step in (x-1, x+1, x*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[x] + 1
                q.append(next_step)        

MAX = 100001
n,k = map(int,input().split()) # 수빈 위치 동생위치
time = [0]*MAX # 0으로 전부 초기화 시켜준 뒤 해당 수가 q에서 나오면 그때 더해 놓은 time을 출력시켜주기 위함

BFS()
