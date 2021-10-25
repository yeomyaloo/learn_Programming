def dfs(n,computers, start,visited):
    visited[start] = True
    
    for i in range(n):
        if visited[i] == False and computers[start][i] == 1:
            visited = dfs(n,computers,i,visited)
    return visited

def solution(n, computers):
    visited = [False] * n
    cnt = 0 
    
    for start in range(n):
        if visited[start] == False:
            dfs(n,computers,start,visited)
            cnt += 1
    return cnt
