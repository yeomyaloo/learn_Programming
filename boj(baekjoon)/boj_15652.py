n, m =  map(int,input().split())
result = []

def dfs(start):
    #append된 값들이 m값만큼 들어와 있다면 출력
    if len(result) == m:
        print(' '.join(map(str,result)))
        return


    for i in range(start, n+1):
        result.append(i)
        #가지치기 작업
        dfs(i)
        result.pop()
      

dfs(1)
