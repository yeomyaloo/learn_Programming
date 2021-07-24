n = int(input())
n_list = list(map(int,input().split()))
list_cnt = 0

for i in n_list:
    cnt = 0

    if i > 1:
        for j in range(2, i+1):
            if i%j == 0:
                cnt +=1
        if cnt == 1:
            list_cnt += 1    
print(list_cnt)    
