import math
r= float(input()) #입력조건 반지름 R이 주어짐

circle = (r**2)*math.pi
taxi = (r**2)*2


print(f'{circle:.6f}')
print(f'{taxi:.6f}')
