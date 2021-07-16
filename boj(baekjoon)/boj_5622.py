a = input().upper()

a_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time =0

for i in a:
    for j in a_list:
        if i in j:
            time += a_list.index(j)+3


print(time)
        
