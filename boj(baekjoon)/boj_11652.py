n = int(input())
d = 2
a = 0

for i in range(n):
    if n % d == 0: #n이 2(부터시작)로 나눠지면 if문 아래 시작 (3...계속)
        print(d)
        n = n // d #n은 나머지로 다시 저장해준다.
    elif n % d != 0: #n이 2로 나뉘지 않을 경우 d+1을 해준다 
        d+=1
