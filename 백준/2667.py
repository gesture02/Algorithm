import sys
from collections import deque


def dfs(i, j):
    global cnt, cnt2
    visited[i][j] = cnt
    inputs[i][j] = 0
    cnt2 += 1
    for a in range(4):
        nx = i + dx[a]
        ny = j + dy[a]

        if 0 <= nx < n and 0 <= ny < n:
            if inputs[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)

def bfs(i, j):
    global cnt, cnt2
    q = deque()
    q.append([i, j])
    visited[i][j] = cnt
    inputs[i][j] = 0
    cnt2 += 1

    while q:
        x, y = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0 <= ny < n:
                if inputs[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    inputs[nx][ny] = 0
                    cnt2 += 1
                    q.append([nx, ny])

n = int(sys.stdin.readline().rstrip())
inputs = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt, cnt2 = 0, 0
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == 0 and inputs[i][j] == 1:
#             cnt += 1
#             cnt2 = 0
#             dfs(i, j)
#             result.append(cnt2)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and inputs[i][j] == 1:
            cnt += 1
            cnt2 = 0
            bfs(i, j)
            result.append(cnt2)

result.sort()
print(cnt)
for i in result:
    print(i)