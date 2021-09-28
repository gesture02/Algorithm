import sys
from collections import deque

def visitable(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(sa, sb, ta, tb):
    q = deque()
    q.append([sa, sb])
    visited[sa][sb] = 1

    while q:
        a, b = q.popleft()

        if a == ta and b == tb:
            return visited[a][b] - 1

        for i in range(8):
            nx = a + x[i]
            ny = b + y[i]

            if visitable(nx, ny) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[a][b] + 1
                q.append([nx, ny])

l = int(sys.stdin.readline().rstrip())
x = [-2, -1, 2, 1, -2, -1, 2, 1]
y = [-1, -2, -1, -2, 1, 2, 1, 2]
for _ in range(l):
    n = int(sys.stdin.readline().rstrip())
    visited = [[0] * n for _ in range(n)]
    sa, sb = map(int, sys.stdin.readline().split())
    ta, tb = map(int, sys.stdin.readline().split())

    print(bfs(sa, sb, ta, tb))