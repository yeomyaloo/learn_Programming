h, m = map(int,input().split())
cooking = int(input())

h += cooking//60
m +=  cooking%60

if m >= 60:
    h += 1
    m -=60
if h >= 24:
    h -= 24
print(h,m)
