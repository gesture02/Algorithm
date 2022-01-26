import sys

n = int(sys.stdin.readline().rstrip())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = inputs[0]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + inputs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + inputs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + inputs[i][2]

print(min(dp[n-1]))