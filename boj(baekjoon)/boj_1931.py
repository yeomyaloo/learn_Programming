import sys
input = sys.stdin.readline

n = int(input())
time = [[0]*2 for _ in range(n)]


for i in range(n):
    start, end = map(int,input().split())
    time[i][0] = start
    time[i][1] = end

#끝나는 시간을 먼저 정렬한 뒤 시작시간 정렬
time = sorted(time, key=lambda a: (a[1],a[0]))
end_time = time[0][1]
cnt = 1


#시작 시간이 회의의 마지막 시간보다 크거나 같을 경우
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt+=1
        end_time = time[i][1]

print(cnt)
