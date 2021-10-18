def solution(N, stages):
    answer = {}
    num = len(stages)

    for i in range(1, N+1):
        if num != 0:
            count = stages.count(i)
            answer[i] = count / num
            #이미 앞서서 실패한 사람을 빼주어야 다음 사람들의 실패율을 정상으로 구할 수 있다.
            num -= count
        else:
            answer[i] = 0
    print(answer)
    return sorted(answer, key=lambda x : answer[x], reverse=True)
