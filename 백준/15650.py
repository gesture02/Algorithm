import sys

def dfs(v):

    if len(s) == m:
        print(*s)

    for i in range(v, n+1):
        if not visited[i]:
            visited[i] = 1
            s.append(i)
            dfs(i)
            visited[i] = 0
            s.pop()


n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
s = []

dfs(1)