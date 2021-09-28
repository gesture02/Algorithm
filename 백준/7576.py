import sys
from collections import deque

def visitable(nx, ny):
    return 0 <= nx < m and 0 <= ny < n

def bfs():

    cnt = -1
    while q:
        cnt += 1
        for _ in range(len(q)):
            a1, b1 = q.popleft()

            for i in range(4):
                nx = a1 + x[i]
                ny = b1 + y[i]

                if visitable(nx, ny) and not visited[nx][ny]:
                    if input[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        input[nx][ny] = 1
    for i in input:
        for j in i:
            if j == 0:
                return -1

    return cnt
n, m = map(int, sys.stdin.readline().split())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
q = deque()

for i in range(m):
    for j in range(n):
        if input[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            q.append([i, j])

print(bfs())