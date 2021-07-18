N = int(input())

cnt = 1

while N > 1: #1이 입력되는 경우는 어차피 바로 print 해주기 때문에 따로 구하지 않음.
    N -= (6*cnt) #6의 배수를 빼며 구해준다.N이 1이 될때까지.
    cnt += 1
print(cnt)
