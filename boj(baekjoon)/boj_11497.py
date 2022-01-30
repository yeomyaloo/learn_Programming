t = int(input())

for _ in range(t):
    n = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    answer = 0
    for i in range(2,n):
        answer = max(answer,abs(tree[i] - tree[i-2]))
    print(answer)
