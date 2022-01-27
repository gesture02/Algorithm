import sys
from collections import deque


def bfs(v):
    q = deque()
    bi[v] = 1
    q.append(v)

    while q:
        w = q.popleft()

        for i in graph[w]:
            if bi[i] == 0:
                bi[i] = -bi[w]
                q.append(i)
            elif bi[i] == bi[w]:
                return False

    return True

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    bi = [0] * (n+1)

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ok = True
    for i in range(1, n+1):
        if bi[i] == 0:
            if not bfs(i):
                ok = False

    print("YES" if ok else "NO")