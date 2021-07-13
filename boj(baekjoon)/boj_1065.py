#x가 등차수열인 경우 - 한수
#등차수열 연속된 두 개의 수의 차이가 일정한 수열.a[i]-a[i+1]==a[i+1]-a[i+2]
# range N (1,1001)
# 한수를 판단하여 한수 수를 더해주는 함수를 만든다.
# N값보다 작은 한수를 출력하기 위해 if문을 사용해 판단한다. 

def hansu(n):
    cnt = 0
    for i in range(1,n+1):
        
        #1000까지의 수를 담고 있을 리스트
        num_list = list(map(int,str(i)))
        
        #100이하의 수는 모두 한수!
        if i < 100:
            cnt += 1

        #리스트에 담긴 100보다 큰 수의 각 자리가 등차수열일 땐 한수
        #한수를 찾기 위한 조건문
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt +=1
    return cnt
n = int(input())
print(hansu(n))
