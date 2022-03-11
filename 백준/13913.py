import sys
from collections import deque
sys.setrecursionlimit(1000000)

def printResult(n, m):
    if n != m:
        printResult(n, result[m])

    print(m, end = ' ')

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0

    while q:
        w = q.popleft()

        for i in (w+1, w-1, 2*w):
            if 0 <= i <= 200000 and dist[i] == -1:
                dist[i] = dist[w] + 1
                result[i] = w
                q.append(i)

n, m = map(int, sys.stdin.readline().split())
dist = [-1] * 200001
result = [0] * 200001

bfs(n)
print(dist[m])
printResult(n, m)