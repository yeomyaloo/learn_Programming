#스택
import sys
input = sys.stdin.readline

def pushx(x):
    return stack.append(x)

def popx():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
    
def sizex():
    return len(stack)

def emptyx():
    if len(stack) == 0:
        return 1
    else:
        return 0
    
def topx():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

n = int(input())
stack = []

for i in range(n):
    s = input().split()
    operator = s[0]
    if operator == "push":
        pushx(s[1])
    elif operator == "pop":
        print(popx())
    elif operator == "size":
        print(sizex())
    elif operator == "empty":
        print(emptyx())
    elif operator == "top":
        print(topx())
        
    
