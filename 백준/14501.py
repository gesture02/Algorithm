import sys

n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + input[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], input[i][1] + dp[i + input[i][0]])

print(max(dp))