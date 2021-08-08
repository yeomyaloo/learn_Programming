import sys #1. input을 썼을 때 시간초과 막기위함 
from collections import Counter

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))
    
lst.sort()
lst_n = Counter(lst).most_common()#3. 최빈값을 알기 위해서. 
#print(lst_n) #[(값, 몇개인지),(값, 몇개인지),(값, 몇개인지),(값, 몇개인지)...]

print(round(sum(lst) / n)) #4. 평균값
print(lst[n // 2]) #5. 중간값
if len(lst_n) > 1:
    if lst_n[0][1] == lst_n[1][1]: #[(0 , 0), (0 , 1), (... , ...), (... , ....)]
        print(lst_n[1][0]) #최빈값을 출력한다. (여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.라는 조건을 만족하기 위함)
    else:
        print(lst_n[0][0])
        #[0][1] / [1][1] : 리스트의 숫자를 세어 놓은 몇개인지.
        #[0][0]/ [1][0] :리스트에 넣은 값(실제 값.)
else:
    print(lst_n[0][0]) #리스트에 값이 하나만 들었을 땐 lst[0]을 출력해준다.
print(lst[-1] - lst[0]) #범위 [-1]은 맨 마지막 요소 / [0]은 맨 처음 요소 젤 큰 값 - 작은 값 = 범위
