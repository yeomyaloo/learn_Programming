cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
result = 0

for i in cro:
    a = a.replace(i,'*')

print(len(a))
