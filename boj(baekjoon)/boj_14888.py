import sys
input = sys.stdin.readline
def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt + 1, result + a[cnt], p - 1, m, mul, div)
    if m:
        dfs(cnt + 1, result - a[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * a[cnt], p, m, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // a[cnt]) if result < 0 else result // a[cnt], p, m, mul, div - 1)
        
n = int(input())#수
a = list(map(int, input().split())) #수열
operator = list(map(int, input().split())) #연산자
max_result = -1000000001
min_result = 1000000001
dfs(1, a[0], operator[0], operator[1], operator[2], operator[3])
print(max_result)
print(min_result)
