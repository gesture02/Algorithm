import sys
def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            s.append(i)
            dfs()
            visited[i] = 0
            s.pop()

n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
s = []

dfs()
