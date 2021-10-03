import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
result = 0
for i in range(n):
    c = int(input())
    if c == 1:
        result += 1
    elif c > 0:
        a.append(c)
    else:
        b.append(c)
a.sort()
b.sort(reverse = True)

while len(a) != 0:
    if len(a) == 1:
        result += a.pop()
    else:
        result += a.pop() * a.pop()
while len(b) != 0:
    if len(b) == 1:
        result += b.pop()
    else:
        result += b.pop() * b.pop()
print(result)

