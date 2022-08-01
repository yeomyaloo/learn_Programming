n = int(input())
top = list(map(int,input().split()))
answer = [0] * n
stack= []

for i in range(n):
    while stack:
        #스택 값
        if stack[-1][1] > top[i]:
            #해당 값의 스택 인덱스에 +1 해주기
            answer[i] = stack[-1][0] + 1
            #다음 값에 또 비교를 위해서 pop해주지 않는다.
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

print(*answer)
