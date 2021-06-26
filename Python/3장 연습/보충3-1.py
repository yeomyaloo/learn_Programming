# 3-1 seq_search()함수를 사용하여 실수 검색하기

from ssearch_while import 3-1

print("실수를 검색합니다.")
print("주의: "End"를 입력하면 종료합니다.")

        
num = 0
x = []

while True:
    s = input(f'x{[num]}: ') #리스트에 넣을 리스트 값
    if s == 'End':
        break
    elif s == 'end':
        break
    elif s == 'END':
        break
    x.append(float(s))
    num +=1


ky = float(input('검색할 값을 입력하세요.: '))


idx = seq_search(x,ky)
if idx == -1:
    print("검색값을 갖는 원소가 존재하지 않습니다.")

else:
    print(f"검색값은 x[{idx}]에 있습니다.")
