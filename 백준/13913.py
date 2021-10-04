import sys
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0

    while q:
        w = q.popleft()
        if w == m:
            nw = m
            for i in range(dist[m] + 1):
                result.append(nw)
                nw = path[nw]
            return
        for nx in (w-1, w+1, w*2):
            if 0 <= nx <= 100000 and dist[nx] == -1:
                dist[nx] = dist[w] + 1
                path[nx] = w
                q.append(nx)
n, m = map(int, sys.stdin.readline().split())
dist = [-1] * 100001
path = [0] * 100001
result = []
bfs(n)
print(dist[m])
print(*list(reversed(result)))