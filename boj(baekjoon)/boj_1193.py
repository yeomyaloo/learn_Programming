#1193

x = int(input())
line = 1

while x > line: # x = 5 
    x -= line # 5, 4, 2 
    line += 1 # 1, 2, 3

if line % 2 ==0 :
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x
print(a,"/",b, sep='')
