import sys
from collections import deque
def dfs(v):
    if visited[v]: return

    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        a = q.popleft()
        print(a, end = ' ')
        for i in graph[a]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [0] * (n+1)
dfs(start)
print()
visited = [0] * (n+1)
bfs(start)