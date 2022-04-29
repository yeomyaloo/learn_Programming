import collections

def BFS(start):
    global answer
    q = collections.deque([1])
    while q:
        x = q.popleft()
        visited[x] = 1

        for i in network[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
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

    BFS(1)
    print(answer)
