import sys

def dfs(s):
    global M, J

    if len(s) == n:
        for i in s:
            if i in ['a','e','i','o','u']:
                M += 1
            else:
                J += 1

        if M >= 1 and J >= 2:
            for i in s:
                print(i, end='')
            print()
        M = 0
        J = 0
        return

    for i in range(m):
        if not visited[i]:
            if s[-1] > input[i]:
                continue
            visited[i] = 1
            s.append(input[i])
            dfs(s)
            visited[i] = 0
            s.pop()

n, m = map(int, sys.stdin.readline().split())
input = list(sys.stdin.readline().split())
input.sort()
visited = [0] * m
M, J = 0, 0
for i in range(m):
    visited[i] = 1
    dfs([input[i]])
    visited[i] = 0