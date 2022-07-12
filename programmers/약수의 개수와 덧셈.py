def div(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    a = list(range(left,right+1))
    res = 0 
    for i in a:
        if div(i)%2 == 0:
            res += i
        else:
            res -= i
            
    return res
ㄴ
