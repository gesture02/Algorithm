import sys

n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if input[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[input[i][0] + i] + input[i][1])

print(max(dp))