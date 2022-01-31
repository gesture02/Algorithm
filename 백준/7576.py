import sys
from collections import deque


def bfs():

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if inputs[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for i in range(m):
    for j in range(n):
        if inputs[i][j] == 1:
            q.append([i, j])
            dist[i][j] = 0
bfs()
answer = max([max(row) for row in dist])
for i in range(m):
    for j in range(n):
        if inputs[i][j] == 0 and dist[i][j] == -1:
            answer = -1
print(answer)