import sys
from collections import deque


def bfs(i, j):
    q = deque()
    q.append([i, j])
    dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and inputs[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)

print(dist[n-1][m-1] + 1)