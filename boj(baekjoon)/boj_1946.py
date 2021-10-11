import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    rank = []
    cnt = 1
    for i in range(n):
        paper, inerview = map(int,input().split())
        rank.append([paper, inerview])

    rank.sort(key=lambda x:x[0]) #서류점수 기준으로 오름차순 정렬
    MAX = rank[0][1] # 첫번째 인터뷰 점수를 기준으로 뒤에 점수보다 높아야 입사 가능

    for i in range(1,n):
        if MAX > rank[i][1]:
            cnt += 1
            MAX = rank[i][1] #다음 비교를 위함
    print(cnt)
