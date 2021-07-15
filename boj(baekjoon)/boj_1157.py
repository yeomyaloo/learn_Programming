#1157



s = input().upper() #입력받은 문자를 대문자화 해서 저장하는 함수 -> s ='aabc'
s_list = list(set(s)) #입력받은 문자를 쪼개는 작업 &중복제거 -> s_list = ['a','b','c']
cnt = []


for i in s_list: # 중복제거한 문자열을 이용해서 원 문자열의 갯수 구하는 작업
    # -> i = a,b,c
    
    count = s.count(i) # 원래 문자열에서 문자들의 숫자 세기 
    cnt.append(count) #빈리스트에 값을 추가 -> cnt =[2,1,1]


if cnt.count(max(cnt)) >=2: #cnt에 저장된 값 중 max값이 2개 이상일 때 = ? 출력
    print("?")

else:
    print(s_list[(cnt.index(max(cnt)))])
