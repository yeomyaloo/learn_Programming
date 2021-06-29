x = []
for i in range(9):
    x.append(int(input()))
sum_x = sum(x)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_x - (x[i] +x[j]) == 100:
            one = x[i]
            two = x[j]
x.remove(one)
x.remove(two)
x.sort()
for i in x:
    print(i)
