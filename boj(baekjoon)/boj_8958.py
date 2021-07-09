T =int(input())

for _ in range(T):
    a = input()
    result = 0 #최종 모두 더한 값 연속된 O와 리셋되어 1로 변환 O의 값을 모두 더한 값
    cnt = 0 #연속적으로 값을 더해주고 초기화시킬 값
    
    for i in range(len(a)):
        if a[i] == "O":
            cnt += 1 #중첩 된다면 계속해서 +1씩 해서 
            result += cnt #최종 값에 더해준다. 
        else:
            cnt = 0 #만약 X가 오게 된다면 cnt값을 0으로 초기화해준다. 
    print(result)
