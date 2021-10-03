import sys
from collections import deque

# def bfs(v):
#     global result
#
#     q = deque()
#     q.append(v)
#     visited[v] = 1
#
#     while q:
#         w = q.popleft()
#         result.append(w)
#         for i in graph[w]:
#             if not visited[i]:
#                 visited[i] = 1
#                 q.append(i)
# def dfs(v):
#     global result
#
#     if visited[v]: return
#
#     visited[v] = 1
#     result.append(v)
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#
# n = int(sys.stdin.readline().rstrip())
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# input = list(map(int, sys.stdin.readline().split()))
# order = [0] * (n+1)
# visited = [0] * (n+1)
# result = []
#
# for i in range(1, n+1):
#     order[input[i-1]] = i
#
# for i in range(1, n+1):
#     graph[i] = sorted(graph[i], key = lambda x: order[x])
#
# dfs(1)
# if result == input:
#     print(1)
# else:
#     print(0)
import math

n = int(sys.stdin.readline().rstrip())
dp = [0] * 100001
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    minv = sys.maxsize
    for j in range(int(math.sqrt(i)) + 1):
        if minv > dp[i-j*j] + 1:
            minv = dp[i-j*j] + 1
    dp[i] = min(dp[i], minv)

print(dp[n])