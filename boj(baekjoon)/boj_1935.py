#해당 수를 해당 문자에 매칭시키고 후위 연산을 진행해준다.

n = int(input())
s = list(input())

stack = []

num = [int(input()) for _ in range(n)]
for x in s:

    if 'A' <= x <= 'Z':
        stack.append(num[ord(x)-ord('A')])

    else:
        b = stack.pop()
        a = stack.pop()
        if x == "+":
            stack.append(a+b)
        elif x == "-":
            stack.append(a-b)
        elif x == "*":
            stack.append(a*b)
        elif x == "/":
            stack.append(a/b) 

print("%.2f" %stack[0])
