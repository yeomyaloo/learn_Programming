import sys

n = int(input())
n_lst=[]
for _ in range(n): 
    n_lst.append(int(sys.stdin.readline()))
    
n_lst.sort()

for i in n_lst:
    sys.stdout.write(str(i)+'\n')
