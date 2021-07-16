cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
result = 0

for i in a:
    for j in cro:
        if i in j:
            result += 1

print(len(a)-result*2)           
            
