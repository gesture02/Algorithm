import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)
if n > 1:
    dp[2] = 3

for i in range(4, n+1, 2):
    dp[i] = 3 * dp[i-2] + 2
    for j in range(2, i, 2):
        dp[i] += dp[j-2] * 2

print(dp[n])