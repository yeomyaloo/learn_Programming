n = int(input())
size = []
for i in range(n) :
    size.append(input().split())
for j in range(n) :
    grade = 1
    for k in range(n) :
        if size[j][0] < size[k][0] and size[j][1] < size[k][1] :
            grade += 1
    print(grade, end= ' ')
