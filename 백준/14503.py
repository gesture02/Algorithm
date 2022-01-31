import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if inputs[r][c] == 0:
        inputs[r][c] = 2
    if inputs[r+1][c] != 0 and inputs[r-1][c] != 0 and inputs[r][c-1] != 0 and inputs[r][c+1] != 0:
        if inputs[r-dx[d]][c-dy[d]] == 1:
            break
        else:
            r -= dx[d]
            c -= dy[d]
    else:
        d = (d+3) % 4
        if inputs[r+dx[d]][c+dy[d]] == 0:
            r += dx[d]
            c += dy[d]
cnt = 0
for i in range(n):
    for j in range(m):
        if inputs[i][j] == 2:
            cnt += 1
print(cnt)