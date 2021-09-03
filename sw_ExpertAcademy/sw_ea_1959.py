T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))

    result = 0
    if N > M:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += mList[j] * nList[i+j]
            if tmp > result:
                result = tmp
    else:
        for i in range(M - N+1):
            tmp = 0
            for j in range(N):
                tmp += nList[j] * mList[i + j]
            if tmp > result:
                result = tmp

    print(f'#{tc} {result}')
