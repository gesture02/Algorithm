import sys

def visitable(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def dfs(cnt, startx, starty, curx, cury, char):
    global isCycle

    if isCycle:
        return

    for i in range(4):
        nx = curx + x[i]
        ny = cury + y[i]

        if cnt >= 4 and startx == nx and starty == ny:
            isCycle = True
            return

        if visitable(nx, ny) and not visited[nx][ny]:
            if input[nx][ny] == char:
                visited[nx][ny] = 1
                dfs(cnt + 1, startx, starty, nx, ny, char)
                visited[nx][ny] = 0

n, m = map(int, sys.stdin.readline().split())
input = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
isCycle = False
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(1, i, j, i, j, input[i][j])
            visited[i][j] = 0

print('Yes' if isCycle else 'No')