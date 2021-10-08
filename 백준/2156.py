import sys

n = int(sys.stdin.readline().rstrip())
input = [0]
input += [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = input[1]
if n > 1:
    dp[2] = dp[1] + input[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + input[i], dp[i-3] + input[i-1] + input[i])

print(dp[n])