import math
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = math.sqrt((x1-x2)**2 +(y1-y2)**2)
    rs = r1 + r2
    rm = abs(r1 - r2) #절대값을 구해주는 함수
    if r == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r == rs or r == rm:
            print(1)
        elif r < rs and r > rm:
            print(2)
        else:
            print(0)    
