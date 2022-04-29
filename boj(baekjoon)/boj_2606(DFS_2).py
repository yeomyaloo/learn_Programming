def DFS(start):
    global answer
    visited[start] = 1
    for i in network[start]:
        if visited[i] == 0:
            DFS(i)
            answer += 1

if __name__ == "__main__":
    computer = int(input())
    pair_Computer = int(input())

    network = [[] for _ in range(computer+1)]
    visited = [0] * (computer + 1)
    answer = 0

    for i in range(pair_Computer):
        a,b = map(int,input().split())
        network[a].append(b)
        network[b].append(a)

    DFS(1)
    print(answer)
