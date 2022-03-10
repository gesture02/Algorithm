import sys
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0

    while q:
        w = q.popleft()

        for i in (w+1, w-1, 2*w):
            if 0 <= i <= 200000 and dist[i] == -1:
                if i == w+1 or i == w-1:
                    dist[i] = dist[w] + 1
                    q.append(i)
                if i == 2*w:
                    dist[i] = dist[w]
                    q.appendleft(i)

n, m = map(int, sys.stdin.readline().split())
dist = [-1] * 200001

bfs(n)
print(dist[m])