import sys


def dfs(path, nextx, cnt):
    global minv

    lastx = path[-1]
    if len(path) == n:
        startx = path[0]
        if input[lastx][startx] != 0:
            minv = min(minv, cnt + input[lastx][startx])
        return

    for i in range(n):
        if not visited[i] and input[nextx][i] != 0:
            visited[i] = 1
            path.append(i)
            dfs(path, i, cnt + input[nextx][i])
            visited[i] = 0
            path.pop()


n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0] * n
minv = sys.maxsize

visited[0] = 1
dfs([0], 0, 0)

print(minv)