day = 0
m = [31,28,31,30,31,30,31,31,30,31,30,31]
w = ['SUN','MON','TUE','WED','THU','FRI','SAT']
x,y = map(int,input().split())

for i in range(x-1):
    day += m[i]

day = (day+y) % 7

print(w[day])
