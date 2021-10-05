import sys
from collections import deque

def visitable(nx, ny):
    return 0 <= nx < m and 0 <= ny < n

def bfs():
    q = deque()
    q.append([0, 0])
    dist[0][0] = 0

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + x[i]
            ny = b + y[i]

            if visitable(nx, ny) and dist[nx][ny] == -1:
                if input[nx][ny] == 0:
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[a][b]
                else:
                    q.append([nx, ny])
                    dist[nx][ny] = dist[a][b] + 1

n, m = map(int, sys.stdin.readline().split())
input = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

bfs()
print(dist[m-1][n-1])