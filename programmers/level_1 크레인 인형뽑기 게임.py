def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)

    #열이 아닌 행을 돌기위함이다. j-1의 범위가 0부터 시작하는 인데스 때
    for j in moves:
        for i in range(n):
            if board[i][j-1] != 0:
                stack.append(board[i][j-1])
                #이미 방문한 곳을 0으로 만들어주어야 다음번에 같은 곳을 가도 뽑은 걸 또 뽑는 일이 없어짐.
                board[i][j-1] = 0
                
                # 스택은 선입후출이니까 제일 나중에 들어온 것과 그 앞에 것이 같은 값이라면 같은 인형이니까 빼주는 작업 진행
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break
    return answer
