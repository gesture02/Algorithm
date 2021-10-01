import sys
def dfs():
    global maxv

    if len(s) == n:
        sums = 0
        for i in range(n-1):
            sums += abs(s[i] - s[i+1])
        maxv = max(maxv, sums)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            s.append(input[i])
            dfs()
            visited[i] = 0
            s.pop()

n = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))
visited = [0] * n
s = []
maxv = 0

dfs()

print(maxv)