

n = int(input())
x = list(map(int,input().split()))
num_count = 0

for i in x : #입력받은 x의 리스트에서 1개씩 꺼내오기
    
    count = 0
    if i == 1 : # x에서 꺼내온 값인 i가 1이라면 다시 처음으로 돌아가서 진행, 1은 소수가 아니다.
        continue
    for j in range(2,i+1): #소수 찾기: 소수는 1과 자기자신만으로 나눠지는 것이 소수이기때문에 count 판별
        if i%j == 0:
            count += 1
    if (count == 1): #count가 1이라면 소수이기 때문에 num_count를 1씩 늘려준다.
        num_count += 1
print(num_count)
