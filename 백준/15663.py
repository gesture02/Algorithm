import sys

def dfs():
    global result
    if len(s) == m:
        result.add(tuple(s[:]))
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            s.append(input[i])
            dfs()
            visited[i] = 0
            s.pop()


n, m = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))
input.sort()
visited = [0] * n
s = []
result = set()
dfs()
result = list(result)
result.sort()
for i in result:
    print(*i)