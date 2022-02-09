import sys
from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    dist[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if inputs[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft([nx, ny])
                if inputs[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    inputs[nx][ny] = 0
                    q.append([nx, ny])

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
print(dist[m-1][n-1])