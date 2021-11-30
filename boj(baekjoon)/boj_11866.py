from collections import deque

n,k = map(int,input().split())

queue = []

for i in range(n):
    queue.append(i+1)

print("<" ,end="")


i = 0
while len(queue) > 1:
    i = i+k
    if i > len(queue):
        i = i %len(queue)
        if i == 0:
            i = i+ len(queue)
    i = i-1
    print(str(queue.pop(i)),end=", ")
print(f"{str(queue.pop())}>")
