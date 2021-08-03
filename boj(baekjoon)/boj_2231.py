n = int(input())
result = 0 

for i in range(1,n+1): #자리수가 아닌 값으로 찾는 문제이기 때문에 설정범위는  1부터 시작합니다. 
    n_list = list(map(int,str(i))) #120이 생성자라고 할 때 1,2,0 나눠서 120 + 3을 해줘야 120이라는 생성자를 찾아낼 수 있다.
    result = i + sum(n_list) #위의 예를 따르면 123이란 숫자가 나오기 위해서 i = 120이 나와야하고 sum(n_list)는 3이 나와야 한다.

    if result == n: #리스트에 들어있는 값을 모두 더한 것을 뺀 i만이 생성자
        print(i)
        break
    elif i == n:
        print(0)
        

