t = int(input())
time = []

for i in range(1,t+1):
    time = list(map(int,input().split()))

    hour = time[0]+time[2]%12
    minute = time[1]+time[3]%60

    if hour > 12:
        hour = hour - 12
    if minute > 60:
        minute -= 60
        hour += 1
    print(f'#{i} {hour} {minute}')

    
