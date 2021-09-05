#15649

from itertools import permutations

n, m = map(int,input().split())
n_lst = []

for i in range(1, n+1):
    n_lst.append(i)

for i in list(permutations(n_lst, m)): # permutations 함수를 통해서 n_lst에 저장된 값을 m개씩 출력하기 위함
    for j in i:
        print(j, end =' ') #줄바꿈 없이

    print()
