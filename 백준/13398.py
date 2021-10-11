import sys

n = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for _ in range(2)]
dp[0][0] = input[0]
dp[1][0] = input[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + input[i], input[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + input[i])

print(max(max(dp[0]), max(dp[1])))