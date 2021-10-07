import sys
from collections import deque

def bfs(v):
    answer = [0, 0]
    visited = [0] * (l + 1)
    dist = [-1] * (l + 1)

    q = deque()
    q.append(v)
    visited[v] = 1
    dist[v] = 0

    while q:
        w = q.popleft()

        for i, weight in graph[w]:
            if visited[i] == 0 and dist[i] == -1:
                visited[i] = 1
                dist[i] = dist[w] + weight
                q.append(i)

                if answer[1] < dist[i]:
                    answer = [i, dist[i]]

    return answer

l = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(l+1)]

for _ in range(l):
    input = list(map(int, sys.stdin.readline().split()))
    root = input[0]

    for i in range(1, len(input)-2, 2):
        graph[root].append([input[i], input[i+1]])
node, result = bfs(1)
node, result = bfs(node)

print(result)