#1983
grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
t = int(input())

for i in range(1, t+1):
    n, k = map(int,input().split())

    scores = []
    
    for j in range(n):
        mid, fin, hw = map(int,input().split())
        scores.append((0.35*mid)+(0.45*fin)+(0.2*hw))
    result = [(score, idx+1) for idx,score in enumerate(scores)]
    result.sort(reverse = True)

    tmp = n//10
    ans = 0
    for c in range(n): 
        if result[c][1] == k:
            ans = c//tmp
    print(f'#{i} {grades[ans]}')
