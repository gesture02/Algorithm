import sys

def dfs(cnt, v):
    global isTrue

    if cnt >= 4:
        isTrue = True
        return

    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, i)
            visited[i] = 0

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [0] * n
isTrue = False
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited[i] = 1
    dfs(0, i)
    visited[i] = 0
    if isTrue:
        break

print(1 if isTrue else 0)