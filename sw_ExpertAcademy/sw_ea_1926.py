n = int(input()) 
lst = [str(i) for i in range( 1 , n+ 1 )] #1

for i in lst: 
    cnt = 0

    #2
    if '3' in i:
        cnt += i.count( '3' )
    if '6' in i:
            cnt += i.count( '6' )
    if '9' in i :
        cnt += i.count( '9' )

    if cnt > 0 :
        print( '-' *cnt, end= ' ' )
    else :
        print(i, end= ' ' )
      
