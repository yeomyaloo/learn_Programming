s = input()

stack = []
res = ""

for i in s:
    if i.isalpha():
        res += i
    else: #연산자인 경우
        if i == "(":
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] =="*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop() #잔여 (여는 괄호 제거를 해주어야 한다.

while stack:
    res += stack.pop()

print(res)
