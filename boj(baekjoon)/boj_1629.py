import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def dc(a,b):
    # 지수가 1일 경우엔 n^1은 n이기 때문에 그대로 값 반환
    if b == 1:
        return a % c
    else:    
        temp = dc(a,b//2) 
        # 지수가 홀수라면 n^2 * n^2 * n을 해주어야 하기에 이렇게 진행
        if b % 2 == 1:
            return temp * temp * a % c
        else:
            return temp * temp % c

print(dc(a,b))
