import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))


for i in range(1,n):
    for j in range(len(tri[i])):
        # 처음 각 라인의 처음과 끝 -> 바로 위의 숫자를 더해준다
        if j == 0:
            tri[i][j] = tri[i][j]+tri[i-1][j]
        # 끝
        elif j == len(tri[i])-1:
            tri[i][j] = tri[i][j]+tri[i-1][j-1]
        #나머지는 왼쪽 대각선, 오른쪽 대각선 중 최댓값을 더해나가 계속 누적시켜주면 된다.
        else:
            tri[i][j] =max(tri[i-1][j-1],tri[i-1][j])+tri[i][j]
print(max(tri[n-1]))
