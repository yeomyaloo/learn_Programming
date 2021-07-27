while True:
    num_list=list(map(int,input().split()))
    num_list.sort()
    
    if sum(num_list) == 0: #만약 리스트의 합이 0일 땐 반복문 종료
        break
    elif num_list[0]**2 + num_list[1]**2 == num_list[2]**2:
        print('right')
    else:
        print('wrong')


