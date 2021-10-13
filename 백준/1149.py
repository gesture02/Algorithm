import sys

n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = input[0]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + input[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + input[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + input[i][2]

print(min(dp[n-1]))