N, M = map(int, input().split())
lst = list()
for i in range(N):
    lst.append(input())
lst2 = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if lst[k][l] != 'W':
                        first_W = first_W+1
                    if lst[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if lst[k][l] != 'B':
                        first_W = first_W+1
                    if lst[k][l] != 'W':
                        first_B = first_B + 1
        lst2.append(first_W)
        lst2.append(first_B)
print(min(lst2))
