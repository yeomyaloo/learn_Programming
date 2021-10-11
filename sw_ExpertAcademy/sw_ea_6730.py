t = int(input())

for tc in range(1, t+1):
    n = int(input())
    steps = list(map(int,input().split()))
    result_asc = []
    result_desc = []
    for i in range(1,len(steps)+1):
        if steps[i-1] < steps[i]:
            result_asc.append(steps[i]-steps[i-1])
        else:
            result_desc.append(steps[i-1] - steps[i])
    print(f'#{tc} {result_asc} {result_desc}')
    
        
