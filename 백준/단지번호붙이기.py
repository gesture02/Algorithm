import sys
from collections import deque

def visitable(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def dfs(i, j):
    global cnt, cnt2, result
    if i < 0 or i > n-1: return
    if j < 0 or j > n-1: return
    if input[i][j] == 0: return

    input[i][j] = 0
    cnt2 += 1
    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)

def bfs(xx, yy):
    global cnt, cnt2, result

    q = deque()
    q.append([xx, yy])
    input[xx][yy] = 0
    visited[xx][yy] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + x[i]
            ny = b + y[i]

            if visitable(nx, ny) and visited[nx][ny] == 0:
                if input[nx][ny] == 1:
                    input[nx][ny] = 0
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    cnt2 += 1

n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
result = []
cnt, cnt2 = 0, 0

# for i in range(n):
#     for j in range(n):
#         if input[i][j] == 1 and not visited[i][j]:
#             cnt2 = 0
#             cnt += 1
#             bfs(i, j)
#             result.append(cnt2+1)
for i in range(n):
    for j in range(n):
        if input[i][j] == 1 and not visited[i][j]:
            cnt2 = 0
            cnt += 1
            dfs(i, j)
            result.append(cnt2)
result.sort()
print(cnt)
for i in result:
    print(i)