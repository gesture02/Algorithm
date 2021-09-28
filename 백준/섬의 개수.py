import sys
sys.setrecursionlimit(100000)
def dfs(i, j):
    global cnt

    if i < 0 or i > m-1: return
    if j < 0 or j > n-1: return
    if input[i][j] == 0: return

    input[i][j] = 0
    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)
    dfs(i - 1, j - 1)
    dfs(i - 1, j + 1)
    dfs(i + 1, j - 1)
    dfs(i + 1, j + 1)
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    input = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    cnt = 0

    for i in range(m):
        for j in range(n):
            if input[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)