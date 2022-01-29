import sys
from collections import deque

def dfs(v):
    if visited[v]: return
    print(v, end = ' ')
    visited[v] = 1

    for i in graph[v]:
        dfs(i)

def bfs(v):
    q = deque()
    visited[v] = 1
    q.append(v)

    while q:
        w = q.popleft()
        print(w, end = ' ')

        for i in graph[w]:
            if visited[i]: continue
            visited[i] = 1
            q.append(i)


n, m, s = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
dfs(s)
print()
visited = [0] * (n+1)
bfs(s)